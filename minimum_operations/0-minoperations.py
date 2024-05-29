#!/usr/bin/python3
"""
Min Operations
"""

def minOperations(n):
    if n <= 1:
        return 0

    op = 0
    d = 2

    while op <= n:
        while n % d == 0:
            op += d
            n //= d
        d += 1

    return op
