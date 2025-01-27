#!/usr/bin/python3
import sys

fileSize: int = 0
status: str = ""
d: dict[str, int] = {}
nbLine = 0

for line in sys.stdin:
    inputSplit = line.split(" ")
    # print(f"debug: {inputSplit}")
    fileSize += int(inputSplit.pop()[:-2])
    status = inputSplit.pop()
    value = d.get(status)
    if value:
        d[status] = value + 1
    else:
        d[status] = 1

    nbLine += 1

    if nbLine % 10 == 0:
        print(f"File size: {fileSize}")
        arrayKeys: [str] = []
        for k in d.keys():
            arrayKeys.append(k)
        arrayKeys.sort()
        for keys in arrayKeys:
            print(f"{keys}:{d[keys]}")