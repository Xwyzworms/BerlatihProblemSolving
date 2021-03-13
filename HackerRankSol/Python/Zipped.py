students,subjects = map(int,input().split())
ans = []
for _ in range(subjects):
    ans.append(map(float,input().split()))
for i in zip(*ans):
   # print( sum(ans[i]) /len(ans[i]) )
    print(sum(i) / len(i))
