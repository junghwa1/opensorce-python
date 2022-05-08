outstr1 = ''
outstr2 = ''

lengs,i=0,0

t = 2
a = ['Open source is source code that is made freely available for possible modification and redistribution.', 'Code is released under the terms of a software license.']


lengs=len(a[0])

for i in range(0,lengs):
    if 'A' <= a[0][i] and a[0][i] <= 'z' :
        outstr1 += a[0][i].upper()
    else :
        outstr1 += a[0][i]
print("1]"+outstr1)
lengs=len(a[1])

i=0
for i in range(0,lengs):
    if 'A' <= a[1][i] and a[1][i] <= 'z' :
        outstr2 += a[1][i].upper()
    else :
        outstr2 += a[1][i]
print("2]"+outstr2)
