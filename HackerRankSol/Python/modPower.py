# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(a,b,m=0):
    print (a**b)
    if m != 0:
        print(pow(a,b,m))

a = int(input())
b = int(input())
c = int(input())
solve(a,b,c)