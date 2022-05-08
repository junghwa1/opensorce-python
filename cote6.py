t = 5
a = ['22220228', '20150002', '01010101', '20140230', '11111111']

for i in range(0,t):
    y=a[i][0:4]
    m=a[i][4:6]
    d=a[i][6:]
    if m=='01' or m=='03' or m =='05' or m =='07' or m =='08' or m =='10' or m =='12':
        if '01' <= d and d <= '31':
            print(i,"] "+y+"/"+m+"/"+d)
        else:
            print(i,"] -1")
    elif m=='04' or m=='06' or m=='09' or m =='11':
        if '01' <= d and d <= '31':
            print(i,"] "+y+"/"+m+"/"+d)
        else:
            print(i,"] -1")
    elif m=='02':
        if '01' <= d and d <= '28':
            print(i,"] "+y+"/"+m+"/"+d)
        else:
            print(i,"] -1")
    else:
        print(i,"] -1")
