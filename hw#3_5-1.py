import random

'''2019038062 염중화'''

## 변수 선언 부분 ##

count=0
conti=0
count_conti=0
count_same=0
dice=[0,0,0,0,0,0]

## 메인 코드 부분 ##

while True:
    for i in range(0,6,1):
        dice[i]=random.randrange(1,7)

    count+=1

    for k in range(0,5,1):
        if (dice[k] == dice[k+1]):
             count_same+=1
    for a in range(0,6,1):
        for b in range(0,6,1) :
            if (dice[a]==dice[b]):
                conti+=1

    if (conti == 6):
        count_conti+=1
        
    if (count_same==5):
        break

    count_same=0
    conti=0

print("6개 주사위가 모두 동일한 숫자가 나옴----> ", dice[0:6])
print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수----> %d"% count)
print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수----> %d"% count_conti)
