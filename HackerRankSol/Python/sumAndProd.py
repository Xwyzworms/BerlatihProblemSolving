import numpy as np

row,col = map(int,input().split())
ans : np.ndarray = np.sum(np.array([input().split() for _ in range(col)],np.int),axis=0)
print(np.prod(ans,axis=None))
 
# Code ini  [input().split() for _ in range(col)] akan ngebuat [[1,2],[1,3],[1,4]]