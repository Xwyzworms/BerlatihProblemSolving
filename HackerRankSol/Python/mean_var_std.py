import numpy as np

row,cols = map(int, input().split())
ans = np.array([input().split() for _ in range(row)],np.int)
print(ans.mean(axis=1))
print(ans.var(axis=0))
print(np.around(ans.std(axis=None),11))
