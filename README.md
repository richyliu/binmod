# binmod

Collection of binary patching tools and techniques. These tools are designed to
add custom code to modify a binary's functionality.

## Techniques

### Dynamically linked

- `dynamic_ld_preload_gdb/`: `LD_PRELOAD` + GDB runtime patch

### Statically linked

- GDB runtime mmap specially crafted executable
- e9patch (AOT patching)
