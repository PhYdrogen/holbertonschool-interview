#!/usr/bin/python3
""" Lockboxes module """


def canUnlockAll(boxes):
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    if n == 0:
        return False

    opened = {0}
    keys = set(boxes[0])

    while keys:
        current_key = keys.pop()

        if 0 <= current_key < n and current_key not in opened:
            opened.add(current_key)
            keys.update(set(boxes[current_key]))

    return len(opened) == n
