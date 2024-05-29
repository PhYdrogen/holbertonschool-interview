#!/usr/bin/python3
"""
Min Operations
"""


def minOperations(n):
    ans = 0
    i = 2
    while i*i<=n:
        if n%i == 0: 
            ans+=i
            n/=i
        else:
            i+=1
    if n!=1:
        ans+=n

    return(int(ans))