#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import *

# Complete the plusMinus function below.
def plusMinus(arr):
    getcontext().prec = 6
    pos = 0
    neg = 0
    other = 0
    n = len(arr)
    for el in arr:
        if el > 0:
            pos+=1
        elif el < 0:
            neg +=1
        else:
            other +=1

    pos = Decimal(float(pos)/n)
    neg = Decimal(neg/n)
    other = Decimal(other/n)

    print(pos, neg, other, sep='\n')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
