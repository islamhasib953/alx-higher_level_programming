#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    cnt = len(sys.argv - 1)
    if cnt == 0:
        print("0 argument.")
    else:
        print("{} argument:".format(cnt))
    for i in range(cnt):
        print("{}: {}".format(i + 1, sys.argv(i + 1)))
