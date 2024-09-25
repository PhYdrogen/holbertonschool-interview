#!/usr/bin/python3
""" Make change calculator 3000 !! """
import typing

def makeChange(coins: typing.List[str], total: int):
    """ Return the minimum number of coins to reach the total """
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != total + 1 else -1
