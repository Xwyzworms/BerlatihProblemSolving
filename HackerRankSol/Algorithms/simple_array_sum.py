

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    ans = 0
    for i in ar:
        ans+=i
    return ans

if __name__ == '__main__':
   print(simpleArraySum([2,4,6,1]))