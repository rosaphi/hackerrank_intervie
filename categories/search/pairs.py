#!/bin/python3

import math
import os
import random
import re
import sys

# Two pointers
def pairs(k, arr):
    arr = sorted(arr)
    i = 0
    j = 0
    res = 0

    while j < len(arr):
        diff = arr[j] - arr[i]
        if diff == k:
            res += 1
            j += 1
        elif diff > k:
            i += 1
        elif diff < k:
            j += 1
    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()