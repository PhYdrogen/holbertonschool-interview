#include <stdlib.h>
#include <stdio.h>
#include "slide_line.h"


int slide_line(int *line, size_t size, int direction)
{
	int linetmp[size];
	for (size_t j = 0; j <= size; j++)
		linetmp[j] = 0;

	int x = 0;
	for (int i = 0; i <= (int)size - 1; i++) {

		if (line[i] != 0 && linetmp[x] == line[i]) {
			linetmp[x] *= 2;
			x++;
			i++;
		}
		if (linetmp[x] != line[i]) {
			linetmp[x] = line[i];
			x++;
		}
		printf("tmp: %d\n", linetmp[x]);

		// if (line[i] != 0) {
		// 	linetmp[x] = line[i];
		// 	printf("line: %d", line[i]);

		// }
	}
	if (direction == 0) { /* Left */
		for (int i = 0; i <= (int)size; i++) {
			line[i] = linetmp[i];
			printf("%d\n", linetmp[i]);
		}

	} else { /* Right */
		for (int k = (int)size - 1; k >= 0; k--) {
			*(line++) = linetmp[k];
			printf("%d\n", linetmp[k]);
		}
	}
	return 1;
}

