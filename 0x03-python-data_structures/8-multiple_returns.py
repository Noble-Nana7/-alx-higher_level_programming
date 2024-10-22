#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        print(sentence[0])
        return len(sentence)
    return None
