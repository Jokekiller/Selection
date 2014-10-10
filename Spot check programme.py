#Harry Robinson
#10-10-2014
#Program stating a students attendance

print("This program will ask for an attendance and see if it is high enough to stay on the course.")
studentAttendance = float(input("Give the attendance: "))
if studentAttendance >= 85:
    print("Your attendance is {0}%. keep it up".format(studentAttendance))
elif studentAttendance < 85:
    print("Your attendace is only {0}%. You must improve it.".format(studentAttendance))
    
