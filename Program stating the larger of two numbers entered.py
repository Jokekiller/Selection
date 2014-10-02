#Harry Robinson
#02-09-2014
#Program stating the larger of two entered numbers

print("This program will state the larger of two entered numbers")
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
if number1 > number2:
    print("{0} is the bigger number".format(number1))
if number1 < number2:
    print("{0} is the bigger number".format(number2))
if number1 == number2:
    print("The numbers are equal")
    
