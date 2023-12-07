#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        mx = list(a_dictionary.key())[0]
        for i in a_dictionary:
            if a_dictionary[i] > a_dictionary[mx]:
                mx = i
        return mx
    return None
