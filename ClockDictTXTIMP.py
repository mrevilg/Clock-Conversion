# prompt user for any time in 24hr hh:mm formatting
user_time = input("Please input any 24hr time in the following format: hh:mm - ")

# TXT import to Dictionary of all possible minutes in 24HRs
time_conversion = {}
with open('minutes.txt') as fileobj:
  for line in fileobj:
      (key, value) = line.split("|")
      time_conversion[key] = value

print(time_conversion)

# iterate over the dictionary keys and return value if same
for key, value in time_conversion.items():
    if key == user_time:
        print (value)
    else:
        print ('unable convert time given')
        break
    