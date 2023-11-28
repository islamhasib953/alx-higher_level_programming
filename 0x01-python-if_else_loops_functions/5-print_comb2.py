#!/usr/bin/python3
for i in range(100):
    if i != 99:
        print("{:s}".format(str(i).rjust(2, '0')), end=", ")
    else:
        print("{:s}".format(str(i).rjust(2, '0')))
