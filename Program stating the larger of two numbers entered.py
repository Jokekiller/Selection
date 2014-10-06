#Harry Robinson
#02-09-2014
#Program stating the larger of two entered numbers

print("This program will state the larger of two entered numbers")
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
number3 = int(input("Give the third number: "))
if number1 > number2 and number1 > number3:
    print("{0} is the bigger number".format(number1))
elif number2 > number1 and number2 > number3:
    print("{0} is the bigger number".format(number2))
elif number3 > number1 and number3 > number2:
    print("{0} is the bigger number".format(number3))
    
    
