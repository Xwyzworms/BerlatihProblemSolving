def count_substring(string, sub_string):
    ans = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            ans+=1
    
    return ans