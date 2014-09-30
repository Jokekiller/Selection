#Harry Robinson
#30-09-2014
#Program stating if two numbers are the same

print("This progrm will state whether two numbers are the same.")

numberOne = int(input("Give 1st number: "))
numberTwo = int(input("Give 2nd number: "))
if numberOne == numberTwo:
    print("The numbers {0} and {1} are the same".format(numberOne, numberTwo))
if numberOne > numberTwo:
    print("first number is too big for number two.")
if numberOne < numberTwo:
    print("first number is too small for number two>")
    
