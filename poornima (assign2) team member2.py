import random
#p=temperature in celsius
p= random.uniform(30.0,70.0)
print("Temperature is",p)
if (p>32):
    print("Alaram is on since the temmperature is above 32 celcius")
else:
    print("Alaram is off since the temmperature is below 32 celcius")
#k=humidity in percentage
k= random.uniform(50,100)
print("Humidity is", k)
if (k>65):
     print("Alaram is on since the humidity is above 65%")
else:
     print("Alaram is on since the humidity is below 65%")
