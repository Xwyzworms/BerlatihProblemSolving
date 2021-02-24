import numpy as np

def solve(theList : list):
    print (np.array(theList).reshape(3,3))

tehList = input().split(" ")
tehList = list(map(int,tehList))
solve(tehList)

