#!/bin/python3

from collections import Counter
import re


def triangular_number(n):
    return (pow(n, 2)+n)//2


# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    exp1 = r'(([a-z])\2*)(?!\1)(?=[a-z]\1)'
    m = re.finditer(exp1, s)
    count += sum([len(x.group(0)) for x in m])

    exp2 = r'([a-z])\1+'
    m = re.finditer(exp2, s)
    count += sum([triangular_number(len(x.group(0)) - 1) for x in m])
    return count


if __name__ == '__main__':
    test_string = 'aaaa'

    n = len(test_string)

    s = test_string

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
