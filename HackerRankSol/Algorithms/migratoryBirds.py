def migratoryBirds(arr):
    ans = []
    dncs =  {1:0,2:0,3:0,4:0,
    5:0}
    num = 1
    for i in range(1,len(arr) +1):
        if arr[i-1] in dncs.keys() :
            dncs[arr[i-1]] = dncs[arr[i-1]] + 1
    
    print(dncs)
    ans = [(key,val) for key , val in dncs.items() if val == max(dncs.values())]
    print(ans)
    if len(ans) > 1:
        return min(ans[0])
    else:
        return min(ans)[0]
        