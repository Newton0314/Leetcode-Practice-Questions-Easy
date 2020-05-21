'''
def countPrimes(n):
    # r stands for remainder
    l = []
    for i in range(2, n):
        l.append(i)
    #print l
    for x in l:
        if x == 2:
            for a in range(2, n/2):
                l.remove(x * a)
        elif x == 3:
            for c in range(3, n/3):
                if x * c in l:
                    l.remove(x * c)
        for y in range(2, int(x**0.5 + 1)):
            r = x % y
            for z in range(2, n / x + 1):
                b = z * x
                if b < n:
                    if b in l:
                        l.remove(b)
            else:
                if r == 0:
                    l.remove(x)
                    #print(x)


    #print l
    print('there are %d prime numbers' % len(l) )
    print(l)
'''


# a better solution
def countPrimes(n):
    if n <= 2:
        return 0
    result = [True] * n
    result[0] = result[1] = False
    for i in range(2, int(n**0.5 + 1)):
        if result[i] == True:
            for j in range(2, (n - 1) / i + 1):
                result[i * j] = False
    return sum(result)


print(countPrimes(4200))


