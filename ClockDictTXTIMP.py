# prompt user for any time in 24hr hh:mm formatting
user_time = input("Please input any 24hr time in the following format: hh:mm - ")

# TXT import to Dictionary of all possible minutes in 24HRs
time_conversion = {}
with open('minutes.txt') as fileobj:
  for line in fileobj:
      (key, value) = line.split("|")
      time_conversion[key] = value

print (time_conversion.get(user_time,"Unknown Input"))


    