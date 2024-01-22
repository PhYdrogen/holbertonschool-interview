#include <stdlib.h>
#include <stdio.h>
#include "sandpiles.h"

/**
 * print_grid - Print 3x3 grid
 * @grid: 3x3 grid
 *
 */
static void print_grid(int grid[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (j)
                printf(" ");
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}

/**
 * is_stable - Check if pile is stable
 * @grid: 3x3 grid
 *
 */
int is_stable(int grid[3][3]) {
  int gridtmp[3][3] = {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };


  for (int i = 0; i < 3; i++)
  {
    for (int j = 0; j < 3; j++)
    {
        if (grid[i][j] > 3) {
            if (i == 0 && j == 0) {
                gridtmp[i+1][j] += 1;
                gridtmp[i][j+1] += 1;
            }
            if (i == 1 && j == 0) {
                gridtmp[i-1][j] += 1;
                gridtmp[i+1][j] += 1;
                gridtmp[i][j+1] += 1;
            }
            if (i == 2 && j == 0) {
                gridtmp[i-1][j] += 1; 
                gridtmp[i][j+1] += 1; 
            }
            if (i == 0 && j == 1) {
                gridtmp[i][j-1] += 1; 
                gridtmp[i+1][j] += 1; 
                gridtmp[i][j+1] += 1; 
            }
            if (i == 1 && j == 1) {
                gridtmp[i+1][j] += 1; 
                gridtmp[i-1][j] += 1; 
                gridtmp[i][j+1] += 1; 
                gridtmp[i][j-1] += 1; 
            }
            if (i == 2 && j == 1) {
                gridtmp[i+1][j] += 1; 
                gridtmp[i-1][j] += 1; 
                gridtmp[i][j+1] += 1; 
                gridtmp[i][j-1] += 1; 
            }
            if (i == 0 && j == 2) {
                gridtmp[i][j-1] += 1; 
                gridtmp[i-1][j] += 1; 
            } 
            if (i == 1 && j == 2) {
                gridtmp[i-1][j] += 1; 
                gridtmp[i+1][j] += 1; 
                gridtmp[i][j-1] += 1; 
            }
            if (i == 2 && j == 2) {
                gridtmp[i-1][j] += 1; 
                gridtmp[i][j-1] += 1; 
            }
            printf("%d ->\n", grid[i][j]);
            print_grid(gridtmp);
            printf("\n");
            grid[i][j] -= 4;
        }
    }
  }
  printf("tmp\n");
  print_grid(gridtmp);
  printf("grid\n");
  print_grid(grid);
  grid = gridtmp;
  return 0; // no issue
}

/**
 * sandpiles_sum - Calculate the sum of sandpiles
 * @grid1: 3x3 grid
 * @grid2: 3x3 grid
 *
 */
int sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
  int gridtemp[3][3];

  for (int i = 0; i < 3; i++)
  { //grid 1
    for (int j = 0; j < 3; j++)
    { //grid 2
      gridtemp[i][j] = grid1[i][j] + grid2[i][j];

    }
  }
  grid1 = gridtemp;

  printf("=\n");
  print_grid(grid1);

  is_stable(grid1);
  printf("=\n");
  print_grid(grid1);

  return 0;
}
