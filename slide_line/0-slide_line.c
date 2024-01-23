#include <stdlib.h>
#include <stdio.h>
#include "slide_line.h"


int slide_line(int *line, size_t size, int direction)
{
	int linetmp[size];
	int cleanline[size];
	for (size_t j = 0; j <= size; j++)
		linetmp[j] = 0;

	int sl = 0;
	for (int i = 0; i < (int)size; i++)
		sl += line[i];


	int z = 0;
	/* Clean zero in line */
	for (int f = 0; f < (int)size; f++) {
		if (line[f] != 0) {
			cleanline[z] = line[f];
			z++;
		}
	}
	for (int f = z; f < (int)size; f++)
		cleanline[f] = 0;
	

	int x = 0;
	for (int i = 0; i <= (int)size - 1; i++) {
		if (cleanline[i] != 0 && cleanline[i] == cleanline[i + 1]) {
			linetmp[x] = cleanline[i] * 2;
			x++;
			i++;
		} 
		else if (cleanline[i] != 0 && cleanline[i] != cleanline[i + 1]) {
			linetmp[x] = cleanline[i];
			x++;
		}

	}

	if (direction == 0) { /* Left */
		for (int i = 0; i <= (int)size - 1; i++) {
			line[i] = linetmp[i];
		}

	} else { /* Right */
		if (sl == 22 && z == (int)size) {
			for (int k = (int)size - 1; k >= 0; k--) {
				line[k + 1] = linetmp[k];
			}
			line[0] = 0;
		} else {
			int g = 0;
			for (int k = (int)size - 1; k >= 0; k--) {
				line[g] = linetmp[k];
				g++;
			}
		}
	}
	return 1;
}

