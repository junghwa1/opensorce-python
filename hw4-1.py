'''2019038062 염중화'''

## 메인 코드 부분 ##

year=int(input("연도를 입력하세요 : "))
if (((year%4)==0)and((year%100)!=0))or((year%400)==0):
    print(year,"은 윤년입니다.")
else:
    print(year,"은 윤년이 아닙니다.")
