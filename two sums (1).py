def twoSums(nums, target):
    m = -1
    n = -1
    for x in nums:
        m += 1
        n = -1
        #print(x, nums.index(x), 'x')
        #print(m, 'm')
        for y in nums:
            n += 1
            #print(y, nums.index(y), 'y')
            #print(n, 'n')
            if x + y == target and m !=n:
                #print (x, y)
                print(m, n)
                return
                
                

twoSums([2,7,11,15], 13)
