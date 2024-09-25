#include "binary_trees.h"
#include <stdlib.h>
#include <stdio.h>

int heap_extract(heap_t **root) {
    heap_t* cursor = *root;
    printf("%d", cursor->n);
    return 0;
}
