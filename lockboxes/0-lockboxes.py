#!/usr/bin/python3
def canUnlockAll(boxes: list[list[int]]):
    a = []
    for e in boxes[0]:
        a.append(e)

    for elem in a:
        for x in boxes[elem]:
            if x not in a and x != 0:
                a.append(x)
    return 1 + len(a) == len(boxes)


# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes)) # True

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes)) # True

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes)) # False