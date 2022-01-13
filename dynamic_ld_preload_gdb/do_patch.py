#!/usr/bin/env -S gdb -x

import gdb
from struct import pack
import re

# NOTE: you may need to modify the variables at the top and the `patch_loc` variable

# whether or not to add 'ret' instruction after patch
# useful if replacing function directly
# otherwise need to be careful of misaligned instructions after patched code
RETURN_DIRECTLY = True
# patch.so to use LD_PRELOAD with
PATCH_FILE = './build/patch.so'

# load the patch
gdb.execute('set environment LD_PRELOAD ' + PATCH_FILE)

gdb.execute('starti')

# address to break at when doing the patch (patch.so must be loaded by this point)
initial_break_addr = '*_start'
file_info = gdb.execute('info file', False, True)
for line in file_info.split('\n'):
    m = re.search(r'Entry point: 0x([0-9a-f]+)', line)
    if m is not None:
        initial_break_addr = '*' + str(int(m.group(1), 16))

# break only once initial patching point
gdb.execute('tbreak ' + initial_break_addr)
gdb.execute('continue')

# replace this with function/address you want to patch
# patch_loc = int(gdb.parse_and_eval('slow').address) # if you have symbols
patch_loc = 0x5555555551b0 # if you do not have symbols

# corresponds with `patched_tramp` in patched_tramp.S
patched_tramp_loc = int(gdb.parse_and_eval('patched_tramp').address)

inferior = gdb.selected_inferior()

# these bytes are written: (8 byte address plus 4 bytes of overhead)
# 48 b8 00 00 00 00 00 00 00 00
# movabs rax,0x12345678
# ff d0
# call   rax
# (optional) c3
# (optional) ret
patch = bytes([0x48, 0xb8]) + pack('Q', patched_tramp_loc) + bytes([0xff, 0xd0])
if RETURN_DIRECTLY:
    patch += bytes([0xc3])
inferior.write_memory(patch_loc, patch)

gdb.execute('continue')
gdb.execute('quit')
