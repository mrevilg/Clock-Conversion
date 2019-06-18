
# from (module) datetime import (class) datetime
from datetime import datetime

# prompt user for any time in 24hr hh:mm formatting
user_time = input("Please input any 24hr time in the following format: hh:mm - ")

# Parse string into datetime:class and then Format into converted version
user_time = datetime.strptime(user_time, '%H:%M').strftime('%I:%M %p')

# print converted version
print (user_time)
