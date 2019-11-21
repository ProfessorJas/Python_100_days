import datetime, time

dt1 = datetime.datetime.fromtimestamp(10000)

dt2 = datetime.datetime.fromtimestamp(time.time())

print(dt1)
# 1970-01-01 10:46:40

print(dt2)
# 2019-11-19 15:42:55.717066