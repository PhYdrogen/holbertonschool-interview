#!/usr/bin/python3
"""
File for functions to validate UTF-8 encoding
"""


def validUTF8(data):
    for i in data:
        if i > 127:
            return False
    return True
