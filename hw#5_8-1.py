'''2019038062 염중화'''

## 변수 선언 부분 ##

instr, outstr = '',''
lengs,i=0,0

## 메인 함수 부분 ##

instr=input("문자열을 입력하세요 : ")
lengs=len(instr)

for i in range(0,lengs):
    if 'A' <= instr[i] and instr[i] <= 'Z' :
        outstr += instr[i].lower()
    elif 'a' <= instr[i] and instr[i] <= 'z' :
        outstr += instr[i].upper()
    else :
        outstr += instr[i]
print("대소문자 변환 결과 --->", outstr)
