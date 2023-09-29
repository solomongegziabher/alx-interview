#!/usr/bin/python3

from sys import stdin


size = 0
code = {"200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for i, line in enumerate(stdin, 1):
        split = line.split(" ")
        if len(split) < 2:
            continue
        if split[-2] in code:
            code[split[-2]] = code[split[-2]] + 1
        size = size + eval(split[-1])
        if i % 10 == 0:
            print("File size: {}".format(size))
            for key in sorted(code.keys()):
                if code[key] > 0:
                    print("{}: {}".format(key, code[key]))
finally:
    print("File size: {}".format(size))
    for key in sorted(code.keys()):
        if code[key] > 0:
            print("{}: {}".format(key, code[key]))
