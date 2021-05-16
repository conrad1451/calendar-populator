from datetime import datetime

# source: https://medium.com/techtofreedom/5-levels-of-handling-date-and-time-in-python-46b601e47f65

# convert a string to a datetime
string_time = '2020-12-25 20:20:20'
t = datetime.strptime(string_time, '%Y-%m-%d %H:%M:%S')
print(t)
# 2020-12-25 20:20:20
print(type(t))
# <class 'datetime.datetime'>

print()

# convert a datetime to a string
now = datetime.now()
string_now = now.strftime('%a,  %d/%m/%Y %H:%M:%S')
print("Date in dd/mm/yyy format: ", string_now)
# Wed,  02/12/2020 23:27:05
string_now = now.strftime('%a,  %m/%d/%Y %H:%M:%S')
print("Date in mm/dd/yyy format: ", string_now)
# Wed,  12/02/2020 23:27:05
print(type(string_now))
# <class 'str'>

print("\n\n\n\n\n")