import operator

'''2019038062 염중화'''

## 변수 선언 부분 #

Str ='''
 내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다.
내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오.
그에게로 가서 나도 그의 꽃이 되고 싶다.
우리들은 모두 무엇이 되고 싶다.
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다.
'''
DicStr={}

## 메인 코드 부분 ##

for ch in Str:
    if'ㄱ' <= ch and ch <= '힣':
        DicStr[ch]=0

for ch in Str:
    if ch in DicStr:
            DicStr[ch]+=1

Strlist = sorted(DicStr.items(), key=lambda x:x[1], reverse=True)

print("원문\n")
print(Str)
print("-----------------------------")
print("문자 \t\t빈도수")
print("-----------------------------")

for i in range(0, len(Strlist)):
    print(Strlist[i][0],"\t\t", Strlist[i][1])
