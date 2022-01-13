#include <asm/unistd.h>
#include <stddef.h>

size_t my_write(int fd, const void *buf, size_t size) {
    size_t ret;
    asm volatile
    (
        "syscall"
        : "=a" (ret)
        //                 RDI      RSI       RDX
        : "0"(__NR_write), "D"(fd), "S"(buf), "d"(size)
        : "rcx", "r11", "memory"
    );
    return ret;
}

int slow(int a) {
  if (a == 0) return 1;
  if (a == 1) return 1;
  return slow(a - 1) + slow(a - 2);
}

// length of "the 40th ..." part
#define STR_INITIAL 30

void _start() {
  int val = slow(42);

  char output[] = "the 42th fibonacci number is:             \n";
  int max_digits = 12;
  for (int i = 0; val > 0; i++) {
    if (i > max_digits) break;
    char digit = val % 10 + '0';
    output[STR_INITIAL + max_digits - i - 1] = digit;
    val /= 10;
  }
  my_write(1, output, STR_INITIAL + max_digits + 1);

  /* exit system call */
  asm("movl $60,%%eax;"
      "syscall"
     :
     : "D" (val)
     );
}
