#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """ can it unlock all ? """
    array = []

    k = 0 if len(boxes) == 1 else 1

    for init in boxes[0]:
        array.append(init)

    for elem in array:
        try:
            for keys in boxes[elem]:
                if keys not in array and keys != 0:
                    array.append(keys)
        except IndexError:
            continue
    return k + len(array) == len(boxes)
