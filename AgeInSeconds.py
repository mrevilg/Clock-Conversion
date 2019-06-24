from datetime import datetime, time

birth_date = input ("Please entre your birthdate yyyy-mm-dd hh:mm:ss")

def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime(f'{birth_date}', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()