import datetime

# print current date and time
print(datetime.datetime.now())
# 2019-11-19 15:39:37.865492

# get the specific time
datetest = datetime.datetime(2019, 9, 30, 22, 22, 22)

print(datetest)
# 2019-09-30 22:22:22

# get 日期的年月日时分秒
print(str(datetest.year) + "-" + str(datetest.month) + '-' + str(datetest.day) + " =>> [" + str(datetest.hour) + ':' + str(datetest.minute) + ':' + str(datetest.second) + ']')
# 2019-9-30 =>> [22:22:22]
