#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sm = 0
    i = 0
    for x in sys.argv:
        if i != 0:
            sum += int(x)
        i += 1
    print("{}".format(sm))
