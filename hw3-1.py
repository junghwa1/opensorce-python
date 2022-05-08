import sys

'''2019038062 염중화'''

## 함수 선언 부분 ##

## 변수 선언 부분 ##

Int = 0
Float = 0.0
Bool = True
Str = ''
List = []
Tuple = ()
Dictionary = {}
Set = set()

## 메인 코드 부분 ##

print('int형 기본크기 --->', sys.getsizeof(Int))
print('float형 기본크기 --->', sys.getsizeof(Float))
print('bool형 기본크기 --->', sys.getsizeof(Bool))
print('str형 기본크기 --->', sys.getsizeof(Str))
print('list형 기본크기 --->', sys.getsizeof(List))
print('tuple형 기본크기 --->', sys.getsizeof(Tuple))
print('dictionary형 기본크기 --->', sys.getsizeof(Dictionary))
print('set형 기본크기->', sys.getsizeof(Set))

