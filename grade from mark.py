#Harry Robinson
#27-10-2014
#Program stating grade from mark

totalMark = int(input("Give the mark: "))
if totalMark >= 81 and totalMark <= 100:
    print("Grade is A")
elif totalMark >= 71 and totalMark <= 80:
    print("Grade is B")
elif totalMark >= 61 and totalMark <= 70:
    print("Grade is C")
elif totalMark >= 51 and totalMark <= 60:
    print("Grafe is D")
elif totalMark >= 41 and totalMark <= 50:
    print("Grade is E")
else:
    print("Grade is U")
