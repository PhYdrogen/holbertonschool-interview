#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes: list[list[int]]) -> bool:
    a = []

    for e in boxes[0]:
        a.append(e)

    for elem in a:
        for x in boxes[elem]:
            if x not in a and x != 0:
                a.append(x)

    return 1 + len(a) == len(boxes)
