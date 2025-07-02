import math 

#area = pi(r**2)

r = float(input("Please enter the radius of the circle: "))
area = round((math.pi * (r**2)), 1)

print(f"The area of the circle is {area}")
