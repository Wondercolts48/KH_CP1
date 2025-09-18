# Kh 2nd Boolean notes

import time
import datetime as date
over = False


print(over)

name = "Ms LaRose"

print(bool(name))


current_time = time.time()
readable_time = time.ctime(current_time)

print(f"Current Time in second since January 1, 1970 (Epoch time): {current_time}")
print(f"Current time: {readable_time} ")

now = date.datetime.now()
hour = now.strftime("%H")
# Month = %m gives us month number ( %b, %B )
#day = %d
#Year = %Y full year or %y for a two digit year
# Hour = %H
# mintues = %M 
#seconds = %S

print(f"Current time according to datetime: {now}")
print(f"hour: {hour}")
print(f"My hour variable is a String: {isinstance(hour, str)}")
print(f"My hour variable is a Integer: {isinstance(hour, int)}")
print(f"My hour variable is a Float: {isinstance(hour, float)}")