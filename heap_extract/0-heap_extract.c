#include "binary_trees.h"
#include <stdlib.h>
#include <stdio.h>

int heap_extract(heap_t **root)
{
    int value;
    heap_t *last_node, *heap_root;

    if (!root || !*root)
        return (0);

    heap_root = *root;
    value = heap_root->n;
    last_node = get_last_node(heap_root);

    if (last_node == heap_root)
    {
        *root = NULL;
        free(heap_root);
        return (value);
    }

    heap_root->n = last_node->n;

    if (last_node->parent->left == last_node)
        last_node->parent->left = NULL;
    else
        last_node->parent->right = NULL;

    free(last_node);
    heapify_down(heap_root);

    return (value);
}
