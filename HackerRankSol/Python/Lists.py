if __name__ == '__main__':
    N = int(input())
    ans = list()
    for i in range(N):
        userInput = input()
        toli = len(userInput.split(" "))
        splitted = userInput.split(" ")
        if ( toli < 2):
            command = splitted[0]
            if(command == "print"):
                print(ans)
            elif(command == "sort"):
                ans.sort()
            elif(command == "pop"):
                ans.pop()
            elif(command == "reverse"):
                ans.reverse()
        elif(toli == 2):
            command = splitted[0]
            nums = int(splitted[1])
            if(command == "append"):
                ans.append(nums)
            elif(command =="remove"):
                ans.remove(nums)
        else:
            command = splitted[0]
            nums = int(splitted[1])
            theIndex = int(splitted[2])
            
            ans.insert(nums,theIndex)
                
                
            
        