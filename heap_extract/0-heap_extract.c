#include "binary_trees.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * heap_size - measures the size of a binary tree
 * @tree: pointer to the root node of the tree to measure the size
 *
 * Return: Size of the tree
 *         0 if tree is NULL
 */
size_t heap_size(const binary_tree_t *tree)
{
    if (!tree)
        return (0);
    return (1 + heap_size(tree->left) + heap_size(tree->right));
}

/**
 * get_last_node - gets the last level-order node in a heap
 * @root: pointer to the root of the heap
 *
 * Return: pointer to the last node
 */
heap_t *get_last_node(heap_t *root)
{
    size_t size;
    unsigned int bit;
    heap_t *node;

    if (!root)
        return (NULL);

    size = heap_size(root);
    for (bit = 1; !(bit & size); bit <<= 1)
        ;
    bit >>= 1;

    for (node = root; bit > 1; )
    {
        if (size & bit)
            node = node->right;
        else
            node = node->left;
        bit >>= 1;
    }

    return (node);
}

/**
 * heapify_down - restores the Max Heap property of a binary heap
 * @root: pointer to the root of the heap
 */
void heapify_down(heap_t *root)
{
    heap_t *node = root, *child;
    int temp;

    while (1)
    {
        if (!node->left)
            break;
        
        if (!node->right || node->left->n > node->right->n)
            child = node->left;
        else
            child = node->right;

        if (node->n >= child->n)
            break;

        temp = node->n;
        node->n = child->n;
        child->n = temp;

        node = child;
    }
}


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
