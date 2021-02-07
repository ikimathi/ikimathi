#func declaration
def km_miles():
    km = int(input("Enter km to convert to miles: "))
    print(str(km) + " km = " + str(km * 0.621371) + " miles")

def m_feet():
    m = int(input("Enter metres to convert to feet: "))
    print(str(m) + " m = " + str(m * 3.28084) + " feet")

def percent_grade():
    percent = int(input("Enter percent to convert to letter grade: "))

    if percent >= 80 and percent <= 100:
        print(str(percent) + "% = " + "A")
    elif percent >= 70 and percent < 80:
        print(str(percent) + "% = " + "B")
    elif percent >= 60 and percent < 70:
        print(str(percent) + "% = " + "C")
    elif percent >= 50 and percent < 60:
        print(str(percent) + "% = " + "D")
    elif percent >= 20 and percent < 50:
        print(str(percent) + "% = " + "E")
    elif percent >= 0 and percent < 20:
        print(str(percent) + "% = " + "F")
    else:
        print("Invalid input!")
    

def acres_sqft():
    acres = int(input("Enter acres to convert to sq feet: "))
    print(str(acres) + " acres = " + str(acres * 43560) + " sq. ft")

def ounce_g():
    ounce = float(input("Enter ounce to convert to grams: "))
    print(str(ounce) + " ounce = " + str(ounce * 28.3495) + " grams")

#program starts
user = str(input("Please enter your name: ")).capitalize()

print("\nHello " + user + ". Welcome to your Personal Unit Converter.")

print("Please choose which conversion you would like to perform:")

print("1 - Convert km to miles")
print("2 - Convert metres to feet")
print("3 - Convert percent to letter grade")
print("4 - Convert acres to sq feet")
print("5 - Convert ounces to grams")

choice = int(input("\nChoice: "))
print()

if choice is 1:
    km_miles()
elif choice is 2:
    m_feet()
elif choice is 3:
    percent_grade()
elif choice is 4:
    acres_sqft()
elif choice is 5:
    ounce_g()
else:
    print("Invalid choice!")

print("Goodbye " +  user + ".")