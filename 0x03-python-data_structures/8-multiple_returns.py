#!/usr/bin/python3
def multiple_returns(sentence):
    a = ""
    if len(sentence) == 0:
        a = None
    else:
        a = sentence[0]
    return len(sentence), a
