#include "sort.h"

/**
 * merge - Merges two subarrays into one sorted array
 *
 * @array: Original array
 * @work_array: Working array for merging
 * @start: Start index of the first subarray
 * @mid: End index of the first subarray and start index of the second subarray
 * @end: End index of the second subarray
 */
void merge(int *array, int *work_array, size_t start, size_t mid, size_t end)
{
    size_t i, j, k;

    printf("Merging...\n");
    printf("[left]: ");
    for (i = start; i < mid; i++)
    {
        if (i > start)
            printf(", ");
        printf("%d", array[i]);
    }
    printf("\n[right]: ");
    for (i = mid; i < end; i++)
    {
        if (i > mid)
            printf(", ");
        printf("%d", array[i]);
    }
    printf("\n");

    i = start;
    j = mid;
    k = start;

    while (i < mid && j < end)
    {
        if (array[i] <= array[j])
            work_array[k++] = array[i++];
        else
            work_array[k++] = array[j++];
    }

    while (i < mid)
        work_array[k++] = array[i++];

    while (j < end)
        work_array[k++] = array[j++];

    for (i = start; i < end; i++)
        array[i] = work_array[i];

    printf("[Done]: ");
    for (i = start; i < end; i++)
    {
        if (i > start)
            printf(", ");
        printf("%d", array[i]);
    }
    printf("\n");
}

/**
 * merge_sort_recursive - Recursive function to implement merge sort
 *
 * @array: Original array
 * @work_array: Working array for merging
 * @start: Start index of the array
 * @end: End index of the array
 */
void merge_sort_recursive(int *array, int *work_array, size_t start, size_t end)
{
    size_t mid;

    if (end - start <= 1)
        return;

    mid = start + (end - start) / 2;

    merge_sort_recursive(array, work_array, start, mid);

    merge_sort_recursive(array, work_array, mid, end);

    merge(array, work_array, start, mid, end);
}

/**
 * merge_sort - Sorts an array of integers in ascending order
 * using the Merge sort algorithm
 *
 * @array: The array to be sorted
 * @size: Number of elements in @array
 */
void merge_sort(int *array, size_t size)
{
    int *work_array;

    if (!array || size < 2)
        return;

    work_array = malloc(sizeof(int) * size);
    if (!work_array)
        return;

    merge_sort_recursive(array, work_array, 0, size);

    free(work_array);
}
