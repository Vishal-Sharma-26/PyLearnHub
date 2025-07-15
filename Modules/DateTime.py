# The datetime module in Python is used to work with dates and times. It allows you to create, format, manipulate, and calculate dates and times easily.
'''
🧱 Main Classes in datetime Module

Class	                     Description
datetime.date	             For working with dates (year, month, day)
datetime.time	             For working with time (hour, minute, second)
datetime.datetime	         Combines both date and time
datetime.timedelta	         For time duration calculations
'''

'''
📚 Useful strftime Codes

Code	            Meaning	                Example
%Y	                Year (4 digits)	        2025
%y	                Year (2 digits)	        25
%m	                Month (01–12)	        07
%d	                Day (01–31)	            13
%H	                Hour (00–23)	        14
%I	                Hour (01–12)	        02
%p	                AM/PM	                PM
%M	                Minutes	                30
%S	                Seconds	                45
%A	                Weekday name	        Sunday
'''


# 1. Importing the Module
import datetime


# 2. Current Date and Time
now = datetime.datetime.now()
print("Current date amd time:", now)


# 3. Current Date Only
from datetime import date

tody = date.today()
print("Today's date:", tody)


# 4. Create Custom Date or Time
from datetime import time, datetime

d = date(2025, 7, 14)
t = time(12, 57, 0)
dt = datetime(2025, 7, 14, 12, 57)

print(d, t, dt)


# 5. Format Date & Time (strftime)
now = datetime.now()

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%I:%M %p"))
print(now.strftime("%A"))


# 6. Parse String to Date (strptime)
date_str = "13-07-2025"
date_obj = datetime.strptime(date_str, "%d-%m-%Y")
print(date_obj)


# 7. Date Arithmetic using timedelta
from datetime import timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)


# 8. Difference Between Two Dates
d1 = date(2025, 7, 13)
d2 = date(2025, 8, 1)

diff = d2 - d1
print("Days between:", diff.days)