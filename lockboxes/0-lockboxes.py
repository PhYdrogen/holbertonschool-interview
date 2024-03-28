#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """ can it unlock all ? """
    array = []

    for init in boxes[0]:
        array.append(init)

    for elem in array:
        for keys in boxes[elem]:
            if keys not in array and keys != 0:
                array.append(keys)

    return 1 + len(array) == len(boxes)
