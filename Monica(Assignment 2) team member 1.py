import random

#Assigning f - fahrenheit


f=random.uniform(10.0,70.0)
print("temperature is",f)
if (f>56):
    print ("Alarm is on since the temperature is above 65 fahrenheit")
else:
    print ("Alarm is off since the temperature is below 65 fahrenheit")

#Assingning a-humidity

h=random.uniform(20,100)
print ("humidity is",a)
if (h>56):
    print("Alarm is on since the humidity is above 36%")
else:
    print("Alarm is off since the humidity is below 36%")
