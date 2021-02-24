import numpy as np
row,col = map(int,input().split())

ans : np.ndarray = np.array([input().strip().split() for _ in range(row)],'int64')
print(ans.transpose())
print(ans.flatten())

