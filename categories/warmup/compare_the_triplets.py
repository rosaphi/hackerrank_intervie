#!/bin/python3

import math
import os
import random
import re
import sys

def compare(pair):
    a, b = pair
    if a > b:
        return (1, 0)
    elif a == b:
        return (0, 0)
    return (0, 1)

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    al = 0
    bob = 0
    for cal, cbob in map(compare, zip(a, b)):
        al += cal
        bob += cbob
    return [al, bob]





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
