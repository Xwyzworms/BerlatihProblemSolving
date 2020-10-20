def isUnique(String):
    
    String = String.lower()
    ans =[]
    for char in String:
        if char in ans:
            return False
        ans.append(char)
    return True
    
    
print(isUnique("Dah gils"))