def birthdayCakeCandles(candles):
    ans =0
    themax = max(candles)
    for i in candles:
        if i == themax:
            ans+=1
    return ans