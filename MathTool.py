# -*- coding: utf-8 -*-

from math import log

def entropy(list):
    """
        calculate shanno entropy of list
        entropy = sum(p*log(p))
    """
    list_prob   = [(i + 0.0) / sum(list) for i in list]
    list_ent    = [i * log(i, 2) for i in list]
    return sum(list_ent)


def Counter(key, counter):
    if key in counter:
        counter[key] += 1
    else:
        counter[key] = 1
