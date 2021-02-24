import numpy as np

row, col = map(int,input().split())
ans : np.ndarray = np.min(np.array([input().split() for _ in range(row)],np.int),axis=1)
print(np.max(ans,axis=0))
