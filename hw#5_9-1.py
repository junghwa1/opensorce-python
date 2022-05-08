## 변수 선언 부분 ##

arr = ['A37B','23CC','88D9','BB8F','3A9A']
arr2= []
chnum=''
numarr=[]

'''2019038062 염중화'''

## 메인 코드 부분 ##

print("정렬 전 데이터 : ", arr[0:5])


for a in range(0,5):
    chnum=''
    arr2= []
    for b in range(0,4):
        if '0' <= arr[a][b] and arr[a][b] <= '9':
            arr2.append(arr[a][b])
    for n in range(0,len(arr2)):
        chnum += arr2[n]
    numarr.append(int(chnum))
    
for k in range(0,4):
    Minindex=k
    for i in range(k+1,5):
        if (numarr[i] < numarr[Minindex]):
            Minindex=i
    arr[k],arr[Minindex] = arr[Minindex],arr[k]
    numarr[k],numarr[Minindex] = numarr[Minindex],numarr[k]

print("정렬 후 데이터 : ", arr[0:5])
