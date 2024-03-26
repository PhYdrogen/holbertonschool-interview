#!/usr/bin/python3
"""
Lockboxes
"""
from collections import deque


def canUnlockAll(boxes):
    """ Lockboxes """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    visited.add(0)
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        keys = boxes[current_box]

        for key in keys:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n