from datetime import date,datetime

print("<======== Today Date =======>")
print(date.today())
print()
print("<======== Current Time  =======>")
current_time = datetime.now().strftime("%H:%M:%S")
print("Current Time =", current_time)
