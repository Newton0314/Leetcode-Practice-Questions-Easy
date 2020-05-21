#PLL stands for palindrome linked list
def PLL(x):
    # type: (object) -> object
    x = list(x)
    a = []
    for i in x:
        if type(i) == int:
            a.append(i)
    b = a[:]
    if b == a.reverse():
        return True
    else:
        return False
#print(PLL([1, 2, 2, 1]))

def PLL2(x):
    """attempt on 2019/12/17
    method of iteration
    didn't understand what a single-linked list was
    """
    x = list(x)
    length = len(x)
    for i in range((length - 1) // 2):
        if x[i] == x[-(i + 1)]:
            continue
        else:
            return False
    return True


print(PLL2([1, 2, 2, 1]))
