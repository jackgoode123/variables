#jack
#variable improvement exercise
#12-09-14

import math

radios = float(input("please enter the radius of the circle: "))

circumference = 2* math.pi * radios
circumference = round(circumference, 2)

area = float(math.pi * radios*2)
area = round(area,2)

print("The circumference of this circle is {0}.".format(circumference))
print("The area of this circle is {0}.".format(area))
