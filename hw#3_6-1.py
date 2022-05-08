## 변수 선언 부분 ##

strnum=""
numnum=0

'''2019038062 염중화'''

## 메인 코드 부분 ##

strnum=input("숫자를 여러 개 입력하세요 :")
print("")
for i in strnum :
    numnum=int(i)
    heart=""
    for k in range(0,numnum,1):
        heart+="\u2665"
    print(heart)
    print("")
