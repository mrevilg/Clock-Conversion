# prompt user for any time in 24hr hh:mm formatting
user_time = input("Please input any 24hr time in the following format: hh:mm - ")

# Dictionary of all possible minutes in 24HRs (import txt function tbc)
time_conversion = {
    '00:00':'12:00 AM',
    '00:01':'12:01 AM',
    '00:02':'12:02 AM',
    '00:03':'12:03 AM',
    '00:04':'12:04 AM',
    '00:05':'12:05 AM',
    '00:06':'12:06 AM',
    '00:07':'12:07 AM',
    '00:08':'12:08 AM',
    '00:09':'12:09 AM',
    # ...etc
}

# iterate over the dictionary keys and return value if same
for HR24, HR12 in time_conversion.items():
    if HR24 == user_time:
        print (HR12)
    else:
        print ("Unknown Input")
        break
    