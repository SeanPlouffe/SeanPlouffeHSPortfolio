# Check for and adjust month input if necessary
def validateMonth(month):
    #this checks if the month is greater than 0 and less than 13 and if so returns that value
    if month > 0 and month < 13:
        return month
    else:
        #if it is less than or equal to 0 or greater than or equal to 13 then it loops until you input a number 1-12 (inclusive)
        while month < 1 or month > 12:
            month = int(input("Invalid month. Please enter value from 1-12: "))
            #once again checking if the month is greater than 0 and less than 13 and if so returning that value
            if month > 0 and month < 13:
                return month

# Check if a given year is a leap year
# Returns 1 if it is a leap year, 0 otherwise
#leap year function
def leap_year(year):
    #This is the formula for leap year, I copied and pasted from the calender project
    #if it is divisible by 400 and 100 then it's a leap year
    if (year % 400 == 0) and (year % 100 == 0):
        leap = 1
    #else if it is divisible by 4 and not divisible by 100 then it is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        leap = 1
    #else it is not a leap year
    else:
        leap = 0
    return leap


# Check for and adjust day input if necessary
def validateDay(month, day, year):
    #this is checking if the year is a leap year so the rest of the function knows that if it's february then it's 28 or 29 days
    if leap_year(year) == 0:
        feb = 28
    elif leap_year(year) == 1:
        feb = 29
    #this checks if the month is one of the 31 day months
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        #this checks if the input day is within 1 and 31 days (inclusive)
        if day > 31 or day < 1:
            #if it is not the correct number it asks the user to input a month until they correctly input a month
            while day > 31 or day < 1:
                day = int(input("Invalid day. Please enter value from 1-31: "))
            return day
        return day
    elif month == 4 or month == 6 or month == 9 or month == 11:
        #this checks if the input day is within 1 and 30 days (inclusive)
        if day > 30 or day < 1:
            #if it is not the correct number it asks the user to input a month until they correctly input a month
            while day > 30 or day < 1:
                day = int(input("Invalid day. Please enter value from 1-30: "))
            return day
        return day
    elif month == 2:
        #this checks if the input day is within 1 and 28-29 days (inclusive)
        if day > feb or day < 1:
            #if it is not the correct number it asks the user to input a month until they correctly input a month
            while day > feb or day < 1:
                day = int(input("Invalid day. Please enter value from 1-" + str(feb) + ": "))
            return day
        return day
    
    

# This function is used to print all events to the user in the format
# Event
# Date: Month Day, Year
def printEvents():
    for i in range(events):
        #this checks the month and outputs the name of the month
        if eventMonth[i] == 1:
            month = "January"
        elif eventMonth[i] == 2:
            month = "February"
        elif eventMonth[i] == 3:
            month = "March"
        elif eventMonth[i] == 4:
            month = "April"
        elif eventMonth[i] == 5:
            month = "May"
        elif eventMonth[i] == 6:
            month = "June"
        elif eventMonth[i] == 7:
            month = "July"
        elif eventMonth[i] == 8:
            month = "August"
        elif eventMonth[i] == 9:
            month = "September"
        elif eventMonth[i] == 10:
            month = "October"
        elif eventMonth[i] == 11:
            month = "November"
        elif eventMonth[i] == 12:
            month = "December"
        #this prints the event day
        print(eventName[i])
        #this prints the date of the month
        print("Date: " + month + " " + str(eventDay[i]) + ", " + str(eventYear[i]))
    


# This function is used to prompt, adjust, and 
# append values to the 4 parallel lists


def addEvent():
    #the next 4 lines take input for the event name, year, month, and day
    event = input("What is the event: ")
    year = int(input("What is the year: "))
    month = validateMonth(int(input("What is the month (number): ")))
    days = int(input("What is the day: "))
    #this makes sure the day is within the correct times of days for the month
    day = validateDay(month, days, year)
    #the next 4 lines add the event name, year, month, and day, to the lists
    eventName.append(event)
    eventYear.append(year)
    eventMonth.append(month)
    eventDay.append(day)
    # Prompt the user for the event details
    
#*********** MAIN **********
#this is globalizing a variable that makes it possible to print the events and event dates the way I did it
global events

#this initializes the list
eventName = []
eventMonth = []
eventDay = []
eventYear = []

#this calls the function to add events
addEvent()
    # Prompt the user to see if they want to enter more events

#this asks if you want to continue adding events or not
end = input("Do you want to enter another date? NO to stop: ")
#this is the initialization of the events variable
events = 1
#this is the loop if you chose to add more events, it loops until you input "NO"
while end != "NO":
    #again calling the addEvent() function
    addEvent()
    #asks if you want to add more events
    end = input("Do you want to enter another date? NO to stop: ")
    #adds 1 to events for every event you add minus the first
    events = events + 1

#prints a barrier because it’s "oh so important"
print("")
print("******************** List of Events ********************")

#this calls the function to print events
printEvents()
