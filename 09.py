import math

r = float(input("Enter the radius of the circle: \n"))

area = (math.pi * r * r)
circumference = (2 * math.pi * r)


print("Radius",r,sep=":", end = "cm.\n")
print("Pi",math.pi,sep=":",end=".\n")
print("Area",area,sep=":",end="sq.cm.\n")
print("Cirumference",circumference,sep=":",end="cm.\n")
