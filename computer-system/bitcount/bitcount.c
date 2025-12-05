#include <assert.h>
#include <stdio.h>

int bitcount (unsigned n) {
    int count = 0;
    while (n) {
        n &= n-1;
        count++;
    }
    return count;
}

int main() {
    int a = 7 & 0x1;
    printf("%d",a);
    assert(bitcount(0) == 0);
    assert(bitcount(1) == 1);
    assert(bitcount(3) == 2);
    assert(bitcount(8) == 1);

    assert(bitcount(0xffffffff) == 32);

    printf("OK\n");
}