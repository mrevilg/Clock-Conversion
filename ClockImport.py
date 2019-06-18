from datetime import datetime

user_time = input("Please input any 24hr time in the following format: hh:mm - ")

user_time = datetime.strptime(user_time, '%H:%M').strftime('%I:%M %p')

print (user_time)
