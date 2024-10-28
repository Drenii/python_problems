import datetime

now = datetime.datetime.now()
print("Current time is")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.astimezone())