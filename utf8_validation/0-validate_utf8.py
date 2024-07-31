#!/usr/bin/python3
"""
File for functions to validate UTF-8 encoding
"""


def validUTF8(data) -> bool:
    def check(num):
            mask = 10000000
            i = 0
            while num & mask:  # 11000110 & 100000
                mask >>= 1
                i += 1
            return i

    for i in range(len(data)):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            current = check(data[i])
            if current != 1: return False
            i += 1
    return True
