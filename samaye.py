from datetime import datetime
tdelta=""
try:
    s1 = input("enter the time to start meeting ")
    s2 = f"{datetime.now().time().hour}:{datetime.now().time().minute}:{datetime.now().time().second}"
    FMT = '%H:%M:%S'
    tsub = datetime.strptime(s1, FMT) - datetime.strptime(s2, FMT)
except:
    print("Enter in this format for example (HH:MM:SS) :- 10:45:45")

print(tsub)