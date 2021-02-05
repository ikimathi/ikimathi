import datetime

date = datetime.date.today()
print("Date:", date)

day = date.weekday()
day_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sunday"]

dayname = day_list[day]

print("Day: ", dayname)


if day <= 4:
    print("Fare: 100")
elif day == 5:
    print("Fare: 60")
elif day == 6:
    print("Fare: 80")
else:
    print("Something is wrong!")
