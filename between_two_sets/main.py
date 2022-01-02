#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    totalX = 0
    is_valid = True
    for item_to_avaliate in range(a[0], b[-1] + 1):
        print(item_to_avaliate)
        is_valid = True
        for item in a:
            if item_to_avaliate % item != 0:
                is_valid = False
                break
        for item in b:
            if item % item_to_avaliate != 0:
                is_valid = False
                break
        if is_valid is True:
            totalX += 1
    return totalX
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
