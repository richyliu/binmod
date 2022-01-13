CC := gcc
CFLAGS := -Wall -O3
BUILD_DIR := build

.PHONY: all target

all: target patch.so

target: target_libc target_no_libc

target_no_libc: $(BUILD_DIR)/target_no_libc.o
	$(CC) $(CFLAGS) -nostdlib -ffreestanding -o $(BUILD_DIR)/target_no_libc $(BUILD_DIR)/target_no_libc.o

$(BUILD_DIR)/target_no_libc.o: target_no_libc.c
	$(CC) $(CFLAGS) -fno-stack-protector -pie -o $(BUILD_DIR)/target_no_libc.o -c target_no_libc.c

target_libc: $(BUILD_DIR)/target.o
	$(CC) $(CFLAGS) -o $(BUILD_DIR)/target $(BUILD_DIR)/target.o

# this patcher works with both -pie and -no-pie
$(BUILD_DIR)/target.o: target.c
	$(CC) $(CFLAGS) -pie -o $(BUILD_DIR)/target.o -c target.c

# patch file must be compiled with -shared
patch.so: $(BUILD_DIR)/patch.o $(BUILD_DIR)/patch_tramp.o
	$(CC) $(CFLAGS) -shared -o $(BUILD_DIR)/patch.so $(BUILD_DIR)/patch.o $(BUILD_DIR)/patch_tramp.o

$(BUILD_DIR)/patch.o: patch.c
	$(CC) $(CFLAGS) -g -o $(BUILD_DIR)/patch.o -c patch.c

$(BUILD_DIR)/patch_tramp.o: patch_tramp.S
	$(CC) $(CFLAGS) -g -o $(BUILD_DIR)/patch_tramp.o -c patch_tramp.S

clean:
	rm build/*
