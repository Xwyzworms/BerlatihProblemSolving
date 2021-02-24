import numpy as np

row,col = map(int,input().split())
ans1 : np.ndarray = np.array([input().split() for _ in range(row)],np.int)
ans2 : np.ndarray = np.array([input().split() for _ in range(row)],np.int)
# default using axis=0
print(np.add(ans1,ans2))
print(np.subtract(ans1,ans2))
print(np.multiply(ans1,ans2))
print(ans1 // ans2) 
print(np.mod(ans1,ans2))
print(np.power(ans1,ans2))
