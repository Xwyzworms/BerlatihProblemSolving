def angryProfessor(k, a):
        studOntime = [std for std in a if std <= 0] 
        print(studOntime)
        if (len(studOntime) >= k):
                return "NO"
        else:
                return "YES"