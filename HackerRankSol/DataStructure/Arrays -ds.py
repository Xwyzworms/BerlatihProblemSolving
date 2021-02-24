def reverseArray(a):
    ans = a.copy()
    size = len(a)
    for i in range ( len(a)//2 ):
        temp = ans[i]
        ans[i] = ans[size - i -1]
        ans[size-i-1] = temp

    return ans