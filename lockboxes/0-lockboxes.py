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
            if len(boxes[elem]) == 0:
                k = k - 1
            for keys in boxes[elem]:
                if keys not in array and keys != 0:
                    array.append(keys)
        except IndexError:
            continue

    array.sort()
    if not (k + len(array) == len(boxes)):
        last = 0
        for chiffre in range(array[0], len(boxes)):
            if last + 1 != chiffre:
                return False
            last = chiffre
        return True
    else:
        return True
