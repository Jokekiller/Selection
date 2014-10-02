#Harry Robinson
# 21-09-2014
#Programme asking for age and displaying if you can vote

def main ():
   age = int(input("Give your age: "))
   if age <= 18:
       print("You can't vote")
   else :
       print ("You can vote")
   retirement = 65 - age    
   if age >= 18:
       print("You can retire in {0} years".format(retirement))
       
       
             
