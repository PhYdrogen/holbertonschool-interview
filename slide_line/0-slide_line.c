#include <stdlib.h>
#include <stdio.h>
#include "slide_line.h"


int slide_line(int *line, size_t size, int direction)
{
	int linetmp[size];
	int cleanline[size];
	for (size_t j = 0; j <= size; j++)
		linetmp[j] = 0;

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
			printf("tmp: %d\n", linetmp[x]);
			x++;
			i++;
		} 
		else if (cleanline[i] != 0 && cleanline[i] != cleanline[i + 1]) {
			linetmp[x] = cleanline[i];
			printf("tmp: %d\n", linetmp[x]);
			x++;
		}

	}
	// if (direction == 0) { /* Left */
	// 	for (int i = 0; i <= (int)size; i++) {
	// 		line[i] = linetmp[i];
	// 		printf("%d\n", linetmp[i]);
	// 	}

	// } else { /* Right */
	// 	for (int k = (int)size - 1; k >= 0; k--) {
	// 		*(line++) = linetmp[k];
	// 		printf("%d\n", linetmp[k]);
	// 	}
	// }
	/* count zero at the end */
	int c = 0;
	for (int z = (int)size - 1; z > 0; z--) {
		if (linetmp[z] != 0) {
			break;
		}
		c++;
	}

	if (direction == 0) { /* Left */
		for (int i = 0; i <= (int)size; i++) {
			line[i] = linetmp[i];
			// printf("%d\n", linetmp[i]);
		}

	} else { /* Right */
		for (int k = (int)size-1; k >= 0; k--) {
		    if (c < 1)
		      line[k] = linetmp[k];
		    if (c > 1)
			    line[k+1] = linetmp[k];
			printf("%d\n", linetmp[k]);
		}
		if (c > 0) {
			for (int l = 0; l < c; l++)
				line[l] = 0;
		}
	}
	return 1;
}

