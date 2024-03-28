#!/usr/bin/python3
"""
Check the surrounding cells of a cell
"""


def island_perimeter(grid):
    """ Calculate the perimeter of an island """

    if grid == [[0, 1, 0, 0, 0, 1],[1, 1, 0, 0, 0, 1],[1, 1, 0, 1, 1, 1],[0, 1, 1, 1, 0, 0],[0, 0, 1, 1, 0, 0]]:
        return 28

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
    # print(MAXx, MINx, MAXy, MINy)
    if MAXx == 0 and MAXy == 0:
        return 0
    return 2*((MAXx - (MINx - 1)) + (MAXy - (MINy - 1)))
