# Enter your code here. Read input from STDIN. Print output to STDOUT
inputs = [input() for i in range(4)]
a,b,c,d = map(int,inputs)
def solve(a,b,c,d):
    return pow(a,b) + pow(c,d)

print(solve(a,b,c,d))