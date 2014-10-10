#Harry Robinson
#10-10-2014
#Gender program

firstName = input("Give your first name: ")
secondName = input("Give your second name: ")
gender = input("Give your gender M/F: ")
if gender == "M":
    print("Mr. {0} {1}".format(firstName,secondName))
elif gender == "F":
    print("Ms. {0} {1}".format(firstName,secondName))
else:
    print("Please enter an appropriate gender")
    

            
