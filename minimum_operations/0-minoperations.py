#!/usr/bin/python3
"""
Min Operations
"""

def minOperations(n):
    h_string = "h"
    op = 0
    if (n <= 1):
        return 0

    for i in range(n):
        if (i == 1):
            deux = n / 2
            trois = n / 3
            # print(deux, trois)
            if ((trois).is_integer() and (deux).is_integer() and trois < deux):
                h_string += h_string
                # print(h_string)

                op += 1
        else:
            h_string = h_string * 2
            # print(h_string, len(h_string))

            op += 2
            if (len(h_string) >= n):
                return op
    return 0
