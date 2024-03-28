#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """ can it unlock all ? """
    array = []

    k = 0 if len(boxes) == 1 else 1

    for init in boxes[0]:
        if init not in array:
            array.append(init)

    for elem in array:
        try:
            for keys in boxes[elem]:
                if keys not in array and keys != 0:
                    array.append(keys)
        except IndexError:
            continue

    array.sort()
    # print(array, "\nk:",k, len(array), len(boxes))
    if not (k + len(array) == len(boxes)):
        for i, chiffre in enumerate(array):
            chiffre = chiffre - 1
            # print(f"i: {i}, chiffre: {chiffre}")
            if i != chiffre:
                return False
        return True
    else:
        return True
