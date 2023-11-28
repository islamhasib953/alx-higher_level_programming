#!/usr/bin/python3
x = -1
for i in range(122, 96, -1):
    if x == -1:
        y = chr(i)
        x *= -1
    else:
        y = chr(i - 32)
        x *= -1
    print("{}".format(y),end="")
