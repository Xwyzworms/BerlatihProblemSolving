def gradingStudents(grades):
    ans= list()

    for grade in grades:
        try: 
            belakangDes = int(str(grade)[1])  
            if grade > 37 :
                if belakangDes > 2 and belakangDes < 5:
                    if belakangDes == 4:
                        ans.append(grade+1)
                    else:
                        ans.append(grade+2)
                elif belakangDes > 7 and belakangDes < 10:
                    if belakangDes == 9:
                        ans.append(grade+1)
                    else:
                        ans.append(grade+2)
                else:
                    ans.append(grade)
            else:
                ans.append(grade)
        except:
                ans.append(grade)
    return ans