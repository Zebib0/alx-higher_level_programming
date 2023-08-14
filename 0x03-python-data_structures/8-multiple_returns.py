#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        str1 = sentence[0]
    else:
        str1 = None
        return (length, str1)
