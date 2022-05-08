'''2019038062 염중화'''

## 함수 선언 부분 ##

def base2(n,list2):
    div_num=int(n)//2
    num=int(n)%2
    list2.append(num)
    if div_num==0:
        return list2
    else:
        return base2(div_num,list2)
    
def base8(n,list8):
    div_num=int(n)//8
    num=int(n)%8
    list8.append(num)
    if div_num==0:
        return list8
    else:
        return base8(div_num,list8)
    
def base16(n,list16):
    div_num=int(n)//16
    num=int(n)%16
    if num>=10:
        num16=format(num, 'x')
        num=num16.upper()
    list16.append(num)
    if div_num==0:
        return list16
    else:
        return base16(div_num,list16)

def linked(lists):
    value=''
    for ch in lists[::-1]:
        value+=str(ch)+" "
        
    return value

## 메인 코드 부분 ##

n=input("10진수 입력--->")
list_num=[]
num=base2(n,list_num)
print("2진수 : ", linked(num))

list_num=[]
num=base8(n,list_num)
print("8진수 : ", linked(num))

list_num=[]
num=base16(n,list_num)
print("16진수 : ", linked(num))
