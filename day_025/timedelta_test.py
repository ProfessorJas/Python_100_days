import datetime
# 用于日期的增加和减少

now = datetime.datetime.now()
print(now)

newdate = now + datetime.timedelta(hours=10)
print(newdate)

newdate = now - datetime.timedelta(days=1)
print(newdate)