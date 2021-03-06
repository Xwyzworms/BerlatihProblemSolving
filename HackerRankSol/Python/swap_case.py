def swap_case(s):
    ans = []
    l = s
    for s in l:

        if(s.islower()):
            ans.append(s.upper())
        elif(s.isupper()):
            ans.append(s.lower())
        else:
            ans.append(s)
    return "".join(ans)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)