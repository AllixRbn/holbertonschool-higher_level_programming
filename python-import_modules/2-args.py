#!/usr/bin/python3

import sys

if __name__ == "__main__":

    args = sys.argv[1:]
    argc = len(args)

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i, argument in enumerate(args, start=1):
        print("{}: {}".format(i, argument))
