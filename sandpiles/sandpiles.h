#ifndef SANDPILE_H
#define SANDPILE_H

int sandpiles_sum(int grid1[3][3], int grid2[3][3]);
int is_stable(int grid[3][3]);
int is_zero(int grid[3][3]);
void shamble(int grid[3][3]);
static void pprint_grid(int grid[3][3]);

#endif
