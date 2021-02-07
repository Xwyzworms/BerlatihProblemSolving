def kangaroo(x1, v1, x2, v2):
        if v1 < v2:
                return "NO"
        else:
                for i in range(10000):
                        if( (x1+v1) == (x2+v2) ):
                                return "YES"
                        x1+= v1
                        x2+= v2
        return "NO"