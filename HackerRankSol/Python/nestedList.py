if __name__ == '__main__':
        ans = {}
        secmax = 0
        for _ in range(int(input())):
                name = input()
                score = float(input())
                ans[name]=score
        
        ans = dict(sorted(ans.items(),key=lambda x : x[0]))
        minfirst = min(ans.values())
        for i in sorted(ans.values()):
                if(i > minfirst):
                        secmax = i
                        break
                
        for key,val in ans.items():
                if(val == secmax ):
                        print(key)