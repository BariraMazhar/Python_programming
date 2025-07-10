leap_year = int(input("Enter year (i.e, 2020) : "))

if(leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
    print("The year you entered is a leap year")
else:
    print("The year you entered is not a leap year")