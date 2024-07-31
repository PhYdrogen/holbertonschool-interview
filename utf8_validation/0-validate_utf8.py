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

    i = 0
    # ok(data)

    while i < len(data):
        lookup = data[i]
        lookupcrop = bin(lookup)[2:]
        if len(lookupcrop) < 8:
            i += 1
            continue
        # print('first', lookupcrop)

        try:
            f = lookupcrop.split('0')[0]
        except IndexError:
            return False
        ##
        # print(data[i])
        ##

        fc = f.count('1')
        if fc - 1 < 1 or fc > 4 or fc > len(data):
            return False
        i += fc
        for x in range(fc):
            try:
                d = bin(data[x+1])[2:]
            except IndexError:
                return True
            d = d.zfill(8)
            ##
            # print(i, d, x, 'fcount', fc)
            ##
            if d.startswith('0') and i >= len(data):
                return True
            if d.index('10') != 0\
                    and i == fc and x + 1 != fc\
                    or i + 1 == len(data)\
                    and d.startswith('11'):
                return False
    return True


def ok(data):
    for i in data:
        k = bin(i).split('b')[1]
        print(i, k.zfill(8), end=" ")
    print()
