def squares(a, b):
        print(a,b)
        b= math.floor(math.sqrt(b)) # Di floor karena agar mendekati nilainya
        a = math.floor(math.sqrt(a-1)) 

        return (b-a )