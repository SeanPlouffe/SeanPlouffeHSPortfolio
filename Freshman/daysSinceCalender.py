#leap year function
def leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        leap = 1
    elif (year % 4 == 0) and (year % 100 != 0):
        leap = 1
    else:
        leap = 0
    return leap
#number of days in month
def number_of_days(month, year):
    #changing february depending on the year
    if leap_year(year) == 0:
        feb = 28
    elif leap_year(year) == 1:
        feb = 29
    #this checks the month and outputs the days
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    elif month == 2:
        days = feb
    return days

#days passed
def days_passed(day, month, year):
    daysPass = -1
    #calculating the days depending on the month
    if month == 1:
        daysPass += day
    elif month == 2:
        daysPass += day + 31
    elif month == 3:
        daysPass += day + 59
    elif month == 4:
        daysPass += day + 90
    elif month == 5:
        daysPass += day + 120
    elif month == 6:
        daysPass += day + 151
    elif month == 7:
        daysPass += day + 181
    elif month == 8:
        daysPass += day + 212
    elif month == 9:
        daysPass += day + 243
    elif month == 10:
        daysPass += day + 273
    elif month == 11:
        daysPass += day + 304
    elif month == 12:
        daysPass += day + 334
    #checking for leap year
    if leap_year(year) == 1 and month > 1:
        daysPass += 1
    return daysPass
#getting the inputs
print("Please enter a date")
#Gathering info
days = int(input("Day: "))
months = int(input("Month: "))
year = int(input("Year: "))
#printing the menu
print("Menu: ")
print("1) Calculate the number of days in the given month.")
print("2) Calculate the number of days passed in the given year.")

menu = int(input())

#printing the outputs
if menu == 1:
    print(number_of_days(months, year))
elif menu == 2:
    print(days_passed(days, months, year))
