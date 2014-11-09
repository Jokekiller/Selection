#Harry Robinson
#29-09-2014
#Improving code in selection

#Harry Robinson
#selection improvement exercise
#26-06-12

month = int(input("Please enter a month as a number between 1-12: "))
year = int(input("Give the year: "))
if year % 4 == 0:
    print("Year is a leap year")
else:
    print("Not a leap year")
if month == 1:
    print("The month you entered is January")
if month == 2:
    print("The month you entered is February")
if month == 3:
    print("The month you entered is March")
if month == 4:
    print("The month you entered is April")
if month == 5:
    print("The month you entered is May")
if month == 6:
    print("The month you entered is June")
if month == 7:
    print("The month you entered is July")
if month == 8:
    print("The month you entered is August")
if month == 9:
    print("The month you entered is September")
if month == 10:
    print("The month you entered is October")
if month == 11:
    print("The month you entered is November")
if month == 12:
    print("The month you entered is December")
elif month > 12:
    print("The month is too high")
elif month < 1 :
    print("The month is too low")
