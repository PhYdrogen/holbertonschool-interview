#!/usr/bin/python3

def canUnlockAll(boxes: list[list[int]]) -> bool:
    """
    Function to check if all boxes in a list can be opened.

    :param boxes: List of lists where inner lists represent keys
    and outer list represents boxes.
    :return: True if all boxes can be opened, False otherwise.
    """

    a = []
    for e in boxes[0]:
        a.append(e)

    for elem in a:
        for x in boxes[elem]:
            if x not in a and x != 0:
                a.append(x)
    return 1 + len(a) == len(boxes)
