# `LD_PRELOAD` with dynamic binaries

Runtime patching of dynamic binaries with `LD_PRELOAD` and GDB.

## Supported binaries

This patcher works with dynamically linked executables. It works regardless of
libc availability and on both PIE and non-PIE binaries.

## Files overview

- `do_patch.py` contains the GDB patching code
- `patch.c` contains the patch itself
- `patch_tramp.S` saves and restores registers, calling the code in `patch.c`
- `target.c` and `target_no_libc.c` are two sample targets

## Building

Run `make all` to build both the target and the patch.

## Executing

Note that you may need to modify the variables in `do_patch.py`, as well as
`patch_loc`, which determines where in the binary to patch. The script is
robust enough to handle stripped binaries, although you will need to hardcode
the patch address (run gdb to see where the function you want to patch is).

To run the patch, do:

```sh
gdb -x do_patch.py build/target
```

Where `build/target` is the target file to patch. Alternatively, you can do
`./do_patch.py build/target` directly.

It may be faster to add the `-nx` flag (which disables .gdbinit files and any
plugins), as well as `-q` to get rid of the copyright message.
