import datetime

time_now = datetime.datetime.now()

day = time_now.day
month = time_now.month
year = time_now.year
hour = time_now.hour
minute = time_now.minute
second = time_now.second

print(f"DATE: {day}/{month}/{year} TIME: {hour}:{minute}:{second}")
