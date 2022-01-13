#include <stdio.h>

unsigned long long fib(int n) {
    unsigned long long a = 0, b = 1, c, i;
    if (n == 0)
        return a;
    for (i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

unsigned long long patched(int a) {
  /* printf("patched func with input: %d\n", a); */

  return fib(a + 1);
}
