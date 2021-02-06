import datetime

date = datetime.date.today()
print("Date:", date)

day = date.weekday()
day_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

dayname = day_list[day]

print("Day: ", dayname)


fare = [100, 60, 80]

if day <= 4:
    print("Fare:", fare[0])
elif day == 5:
    print("Fare:", fare[1])
elif day == 6:
    print("Fare:", fare[2])
else:
    print("Something is wrong!")
