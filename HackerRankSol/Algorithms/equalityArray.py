#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):

    dictans = {}
    
    for i in (arr):
        if i in dictans:
            dictans[i] += 1
        else:
            dictans[i] = 1
    
    maxKeys = max(dictans, key= dictans.get)
    
    return abs(dictans[maxKeys] - len(arr))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
