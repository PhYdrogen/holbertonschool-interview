#include <stdio.h>
#include "menger.h"

/**
 * isFilled - Determines if a cell should be filled in a Menger sponge
 * @x: Row coordinate
 * @y: Column coordinate
 * @size: Current size of the square being considered
 *
 * Return: 1 if the cell should be filled ('#'), 0 otherwise (' ')
 */
int isFilled(int x, int y, int size)
{
	if (size == 1)
		return (1);
	int s = size / 3;
	int x_block = x / s;
	int y_block = y / s;

	if (x_block == 1 && y_block == 1)
		return (0);
	return (isFilled(x % s, y % s, s));
}

/**
 * menger - Draws a 2D Menger Sponge
 * @level: The level of the Menger Sponge to draw
 *
 * Description: Prints a Menger sponge of the specified level.
 *              If level is lower than 0, the function does nothing.
 *              The sponge is printed using '#' for filled cells and
 *              ' ' for empty cells.
 */
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
