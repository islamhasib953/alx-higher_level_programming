#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    if my_list:
        try:
            for i in range(x):
                print(my_list[i], end="")
                cnt += 1
        except IndexError:
            None
        print()
        return cnt
