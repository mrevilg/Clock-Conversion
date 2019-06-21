# from 24 hour to 12 hour format 

# obtain data as string from user
user_input = input("Please input any 24hr time in the following format: hh:mm - ")

# split string at ":" 
user_input = user_input.split(":")

# convert hr:mm from string to int
_hr = int(user_input[0])
_min = int(user_input[1])

# handle AM/PM 
ampm = ""
if _hr == 12:
  ampm = "PM"
elif _hr == 0:
  ampm = "AM"
  _hr = 12
elif _hr >= 12:
  ampm = "PM"
  _hr = _hr - 12
else:
  ampm = "AM"
  
# display converted time
print(str(_hr) + ":" +str(_min) + " " + ampm)
