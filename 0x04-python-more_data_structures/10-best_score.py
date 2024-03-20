#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxValue = 0
    maxKey = None
    for k, v in a_dictionary.items():
        if v > maxValue:
            maxValue = v
            maxKey = k
    return maxKey
