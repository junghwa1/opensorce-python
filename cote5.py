t = 10
a = [9, 15, 54, 369, 634, 1053, 2954, 4234, 5424, 9531]
b = [2, 6, 6, 15, 20, 34, 50, 89, 123, 9999]


for i in range(0, t):
    if a[i]<b[i]:
        small=a[i]
    else:
        small=b[i]
    for k in range(1,small+1):
            if (a[i] % k == 0) and (b[i] % k == 0):
                maxed = k 
    print("%d] %d"%(i, maxed))
    
