#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid: list[list[int]]):
    """ Calculate perimeter """

    array = []
    for x, row in enumerate(grid):
        for y, elem in enumerate(row):
            if elem == 1:
                array.append({'x':x, 'y':y})

    MAXx = 0
    MAXy = 0
    MINx = 100
    MINy = 100
    for obj in array:
        if obj['x'] < MINx:
            MINx = obj['x'] 
        if obj['y'] < MINy:
            MINy = obj['y'] 
        if obj['x'] > MAXx:
            MAXx = obj['x'] 
        if obj['y'] > MAXy:
            MAXy = obj['y']
    print(MAXx, MINx, MAXy, MINy)

    return 2*((MAXx - (MINx - 1)) + (MAXy - (MINy - 1)))