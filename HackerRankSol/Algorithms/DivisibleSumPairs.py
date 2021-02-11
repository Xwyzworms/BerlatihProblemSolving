import math 
import os
import random
import re
import sys

def divisibleSumPairs(n,k,ar):
    ans = 0
    for i in range(n):
        for j in range(n):
            if (i < j ) and ((ar[i] + ar[j]) % k == 0):
                ans +=1
    return ans

if __name__ == '__main__':
    
    nk = input().split()

    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int,inpput().rstrip().split()))

    result= divisibleSumPairs(n,k,ar)
    