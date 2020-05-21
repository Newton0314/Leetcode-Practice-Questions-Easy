# RTI stands for roman to integer
def RTI(r):
    num = 0
    r = list(r)
    r.append('')
    for i in r:
        if i == 'I':
            if r[r.index(i) + 1] == 'V' and len(a) < (r.index(i)+ 1):
                num += 4
                r.remove(r[r.index(i) + 1])
            elif r[r.index(i) + 1] == 'X':
                num += 9
                r.remove(r[r.index(i) + 1])
            else:
                num += 1
        elif i == 'V':
            num += 5
        elif i == 'X':
            if r[r.index(i) + 1] == 'L':
                num += 40
                r.remove(r[r.index(i) + 1])
            elif r[r.index(i) + 1] == 'C':
                num += 90
                r.remove(r[r.index(i) + 1])
            else:
                num += 10
        elif i == 'L':
            num += 50
        elif i == 'C':
            if r[r.index(i) + 1] == 'D':
                num += 400
                r.remove(r[r.index(i) + 1])
            elif r[r.index(i) + 1] == 'M':
                num += 900
                r.remove(r[r.index(i) + 1])
            else:
                num += 100
        elif i == 'D':
            num += 500
        elif i == 'M':
            num += 1000
        elif i == '':
            return(num)
    return(num)

print(RTI('DCXXI'))






    
    
    
