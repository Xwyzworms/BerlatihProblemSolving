import re
N=input()
for i in range(int(N)):
    soal = input()
    if(re.match(r'^[789]\d{9}$',soal)):
        print("YES")
    else:
        print("NO")