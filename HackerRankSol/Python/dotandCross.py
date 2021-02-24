import numpy as np

row = int(input())
ans1 :np.ndarray = []
ans2 : np.ndarray = []

ans1 = np.array([input().split() for i in range(row) ],np.int)

ans2 = np.array([input().split() for i in range(row)],np.int)


print(np.dot(ans1 , ans2))
