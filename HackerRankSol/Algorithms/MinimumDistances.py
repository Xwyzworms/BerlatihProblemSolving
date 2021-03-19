#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    minim = 1000
    indexTwo = 0
    for i in a:
        if a[indexTwo] in a:
            temp = indexTwo - a.index(i)
            if temp < minim and temp != 0:
                minim = temp
                
        indexTwo +=1 
    if minim == 1000:
        return -1
    return minim

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
