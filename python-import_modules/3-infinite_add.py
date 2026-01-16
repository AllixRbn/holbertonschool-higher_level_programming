#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    argc = len(args)
    result = 0

    for i in range(argc):
        result += int(args[i])

    print(result)
