#include <stdio.h>
#include "menger.h"

int isFilled(int x, int y, int size)
{
    if (size == 1)
        return 1;
    int s = size / 3;
    int x_block = x / s;
    int y_block = y / s;
    if (x_block == 1 && y_block == 1)
        return 0;
    return isFilled(x % s, y % s, s);
}

void menger(int level)
{
    if (level < 0)
        return;
    int size = 1;
    for (int i = 0; i < level; i++)
        size *= 3;
    for (int row = 0; row < size; row++)
    {
        for (int col = 0; col < size; col++)
        {
            if (isFilled(row, col, size))
                putchar('#');
            else
                putchar(' ');
        }
        putchar('\n');
    }
}
