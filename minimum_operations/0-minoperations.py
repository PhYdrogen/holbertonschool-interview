#!/usr/bin/python3
"""
Min Operations
"""

def minOperations(n):
    if n % 2 == 1:
        return n
    else:
        copy = n // 2
        paste = n - copy
        return copy + paste