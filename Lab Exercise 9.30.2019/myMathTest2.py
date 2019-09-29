from myMath import *

radius = float(input("Enter the radius of a sphere: "))
temp = input("Enter the length, width, and height of a cuboid(seperated by spaces): ")
length, width, height = temp.split()
length = float(length)
width = float(width)
height = float(height)
poly = [5, 3.2, 7.1, 0, 6.9]
x = -13

print ("Surface area of sphere = ", sphereArea(radius))
print ("Volume of sphere = ", sphereVolume(radius))
print ("Surface area of cuboid = ", cuboidArea(length, width, height))
print ("Volume of cuboid = ", cuboidVolume(length, width, height))
print (polyPrettyPrint(poly), '=', evaluatePoly(poly, x))

