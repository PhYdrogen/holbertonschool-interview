#!/usr/bin/python3
"""
File for functions to validate UTF-8 encoding
"""


def validUTF8(data) -> bool:
    if len(data) == 0:
        return True

    if data[0] < 128:
        for i in data:
            if i > 127:
                return False
        return True

    f = data[0]
    f = bin(f)[2:]
    try:
        f = f.split('0')[0]
    except IndexError:
        return False
    # ok(data)
    # print(data[0])
    if f.count('1') - 1 < 1 or f.count('1') > 4:
        return False
    for i in range(f.count('1') - 1):
        try:
            d = bin(data[i+1])[2:]
        except IndexError:
            return False
        d = d.zfill(8)
        # print(d, i)
        try:
            if d.index('10') != 0 and i == f.count('1'):
                return False
        except ValueError:
            return False
    return True


def ok(data):
    for i in data:
        print(bin(i), end=" ")
