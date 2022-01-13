#include <stdio.h>

unsigned long long slow(int a) {
  if (a == 0) return 1;
  if (a == 1) return 1;
  return slow(a - 1) + slow(a - 2);
}

int main() {
  for (int i = 35; i < 50; ++i)
    printf("%u %llu\n", i, slow(i));
}
