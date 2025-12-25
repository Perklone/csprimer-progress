#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#define STARTING_CAPACITY 8

typedef struct DA {
  void** items;
  int length;
  int capacity;
} DA;


DA* DA_new (void) {
  DA* da = malloc(sizeof(DA));
  da->items = malloc(STARTING_CAPACITY * sizeof(void*));
  da-> capacity = STARTING_CAPACITY;

  return da;
}

void DA_free(DA *da) {
  free(da->items);
  free(da);

  return;
}

int DA_size(DA *da) {
  return da->length;
}

void DA_push (DA* da, void* x) {
  if(da->length == da->capacity) {
    da->capacity <<= 1;
    da->items = realloc(da->items, da->capacity * sizeof(void *));
    printf("Resized to %d\n",da->capacity);
  }

  da->items[da->length++] = x;
  return;
}

void *DA_pop(DA *da) {
  if (da->length == 0) return NULL;

  void* address = da->items[da->length - 1];
  da->items[da->length--] = NULL;

  return address;
}

void DA_set(DA *da, void *x, int i) {
  // TODO set at a given index, if possible
  if(i < 0 || i > (da->length - 1)) return;
  da->items[i] = x;
}

void *DA_get(DA *da, int i) {
  // TODO get from a given index, if possible
  return da->items[i];
}

int main() {
    DA* da = DA_new();

    assert(DA_size(da) == 0);

    // basic push and pop test
    int x = 5;
    float y = 12.4;
    DA_push(da, &x);
    printf("%d\n", *(int*)&x);
    DA_push(da, &y);
    assert(DA_size(da) == 2);

    assert(DA_pop(da) == &y);
    assert(DA_size(da) == 1);

    assert(DA_pop(da) == &x);
    assert(DA_size(da) == 0);
    assert(DA_pop(da) == NULL);

    // basic set/get test
    DA_push(da, &x);
    DA_set(da, &y, 0);
    assert(DA_get(da, 0) == &y);
    // Fetched from Array of void* -> Cast it to a float pointer
    // type is now float* -> dereference it to get the value of y.
    printf("%f\n", *(float*)&y);
    DA_pop(da);
    assert(DA_size(da) == 0);

    // expansion test
    DA *da2 = DA_new(); // use another DA to show it doesn't get overriden
    DA_push(da2, &x);
    int i, n = 100 * STARTING_CAPACITY, arr[n];
    for (i = 0; i < n; i++) {
      arr[i] = i;
      DA_push(da, &arr[i]);
    }
    assert(DA_size(da) == n);
    for (i = 0; i < n; i++) {
      assert(DA_get(da, i) == &arr[i]);
    }
    for (; n; n--)
      DA_pop(da);
    assert(DA_size(da) == 0);
    assert(DA_pop(da2) == &x); // this will fail if da doesn't expand

    DA_free(da);
    DA_free(da2);
    printf("OK\n");
}
