#Harry Robinson
#08-10-2014
#Program stating the gross pay and extra hours

hourlyRate = float(input("Give you're hourly rate: "))
hoursWorked = float(input("Give the hours you have worked this week: "))
if hoursWorked >= 0 and hoursWorked <= 60:
    print("Enter a value in the range of 0-60.")
    if hoursWorked < 40:
        grossPay = hourlyRate * hoursWorked
        print("grossPay = {0}".format(grossPay))
    elif hoursWorked >= 40:
        extraHours = hoursWorked - 40
        extraPay = hourlyRate * 1.5
        grossPay = (hourlyRate * 40) + (extraHours * extraPay)
        print("grossPay = {0}".format(grossPay))
if hoursWorked <0 or hoursWorked > 60 :
    print("Give a vlue in the range 0-60")
    
