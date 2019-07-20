#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import chain
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    # Write your code here
    ld_sum = 0
    rd_sum = 0

    for i in range(n):
        for j in range(n):
            if i==j:
                ld_sum += arr[j][i]
                rd_sum += arr[n-i-1][j]
    return(abs(ld_sum-rd_sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
