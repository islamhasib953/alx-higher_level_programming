#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            str = str.replace(i, chr(ord(i)-32))
    print(str)


uppercase("best")
uppercase("Best School 98 Battery street")
