from datetime import *
from time import *

'''2019038062 염중화'''

## 변수 선언 부분 ##

tm=None
tm=localtime()
present=str(tm.tm_year)+'/'+ str(tm.tm_mon)+'/'+str(tm.tm_mday)

## 메인 코드 부분 ##

start_date=input("시작 날짜(연/월/일) ---> ")
year,month,day=start_date.split('/')
sday=date(int(year),int(month),int(day))
year,month,day=present.split('/')
pday=date(int(year),int(month),int(day))
difday=pday-sday
difday=difday.days

weeks=['월','화', '수', '목', '금', '토', '일']


compare=datetime.strptime(start_date,"%Y/%m/%d")
print(start_date,"부터 오늘(",present,")까지는 ",difday,"일이 지났습니다")
print("그리고 오늘은 ", weeks[tm.tm_wday], "요일입니다.")
