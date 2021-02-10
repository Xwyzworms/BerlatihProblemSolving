def findDigits(n):
        strN = [int(dig) for dig in str(n)]
        ans = 0
        for i in strN:
                if (i != 0):
                        if n % i == 0:
                                ans +=1
        
        return ans
