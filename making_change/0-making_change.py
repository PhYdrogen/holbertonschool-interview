#!/usr/bin/python3
""" Make change calculator 3000 !! """
import typing

def makeChange(coins: typing.List[str], total: int):
    change = 0
    for money in coins:
        if (change + money < total):
            change += money
    if change == total:
        return 0
    return -1