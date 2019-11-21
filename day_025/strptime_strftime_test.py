import datetime, time, _strptime

datestr = time.strptime('2019-9-30 22:10:00', '%Y-%m-%d %H:%M:%S')
print(datestr)

print(datetime.datetime.now().strftime('%a, %b %d %H:%M'))      # get the current time