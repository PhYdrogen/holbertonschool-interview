#!/usr/bin/python3
"""
Function to check if all boxes in a list can be opened.

:param boxes: List of lists where inner lists represent keys
and outer list represents boxes.
:return: True if all boxes can be opened, False otherwise.
"""


def canUnlockAll(boxes: list[list[int]]) -> bool:
    """ Open all the boxes """

    a = []
    #Create an array
    for e in boxes[0]:
        #loop over the first box

        a.append(e)
        #add to the array the element

    for elem in a:
        #loop over the array the existing box 
        for x in boxes[elem]:
            #each key of box 
            if x not in a and x != 0:
                #x not 0 and not already in box 
                a.append(x)
                #add to array 
    #return true or false 
    return 1 + len(a) == len(boxes)
