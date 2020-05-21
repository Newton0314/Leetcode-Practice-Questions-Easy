def Reverse(x):
    if x > 0:
        l = list(str(x))
        l.reverse()
        result = int(''.join(l))
        if result > 2**31-1:
            return 0
        print result
        return
    elif x < 0:
        x = x * (-1)
        l = list(str(x))
        l.reverse()
        result = int(''.join(l))
        result *= -1
        if result < -2**31:
            return 0
        print (result)
        return
    
Reverse(320)
    
