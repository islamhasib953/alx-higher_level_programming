#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for i in str:
        if i == ' ':
            str2 += ' '
        if ord(i) >= 65 and ord(i) <= 90:
            str2 += i
        else:
            str2 += chr(ord(i)-32)
    print(str2)


uppercase("best")
uppercase("Best School 98 Battery street")
