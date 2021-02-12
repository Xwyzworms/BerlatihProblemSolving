# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = input()

for i in range(int(n)):
    if(re.match(r"^[+-.]?[0-9]*\.[0-9]+$",input())):
        print(True)
    else:
        print(False)
