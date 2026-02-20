from datetime import date
import datetime
from datetime import datetime
from datetime import timedelta

# today = date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)

# print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# now = datetime.now()
# print(now)                      # 2021-07-08 07:34:46.549883
# day = now.day                   # 8
# month = now.month               # 7
# year = now.year                 # 2021
# hour = now.hour                 # 7
# minute = now.minute             # 38
# second = now.second
# timestamp = now.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# data_string = "5 Dec, 2025"
# print("data_string =", data_string)

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)