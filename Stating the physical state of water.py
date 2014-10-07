#Harry Robinson
#07-10-2014
#Program stating the physical state of water

print("This program will state the state of water")
waterTemperature = float(input("Give the temperature of your water: "))
if waterTemperature <= 0:
    print("Water has frozen")
if waterTemperature >= 100:
    print("Water is boiling")
elif waterTemperature > 0 and waterTemperature < 100:
    print("Water is neither boiling or frozen")
    
