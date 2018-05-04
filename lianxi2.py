import datetime
s=datetime.datetime.now()
# strftime把日期变成
print s.strftime('%Y%m%d%H%M%S')

case_id = s.strftime('%Y%m%d%H%M%S') + str(s).split('.')[1]
print case_id
