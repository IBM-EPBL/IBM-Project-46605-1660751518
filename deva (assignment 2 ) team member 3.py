import random

#Assigning x- celcius


f=random.uniform(10.0,80.0)
print("temperature is",f)
if (f>39):
    print ("Alarm is on since the temperature is above 39 celcius")
else:
    print ("Alarm is off since the temperature is below 39 celcius")

#Assingning y-humidity

y=random.uniform(20,100)
print ("humidity is",y)
if (y>51):
    print("Alarm is on since the humidity is above 51%")
else:
    print("Alarm is off since the humidity is below 51%")
