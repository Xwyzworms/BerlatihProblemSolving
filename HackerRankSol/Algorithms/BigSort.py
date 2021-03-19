#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the bigSorting function below.
def solve(a):
    return sorted(a,key=len)
if __name__ == '__main__':

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    unsorted.sort()
    result =solve(unsorted)
    print("\n".join(result))