#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - check is palindrome
 * @head: pointer to list
 * Return: int if 1 is, 0 is not
 */
int is_palindrome(listint_t **head)
{
    int array[1024];
    listint_t *current;
    int cp = 0;

    while (head != NULL)
    {
        current = *head;
        array[cp] = current->n;
        cp += 1;
        if (current->next == NULL)
        {
            break;
        }
        head = &current->next;
    }
    int j = 0;
    int k = cp % 2;

    for (int i = cp - 1; i > 0; i--)
    {
        if (k == 1 && i == cp / 2)
        {
            break;
        }
        if (array[i] != array[j])
        {
            return 0;
        }
        j++;
    }
    return 1;
}
