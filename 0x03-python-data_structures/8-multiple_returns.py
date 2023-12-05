#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        res_tuple = (len(sentence), sentence[0])
    else:
        res_tuple = (len(sentence), "None")
    return res_tuple
