import myMath

radius = float(input("Enter the radius of a sphere: "))
temp = input("Enter the length, width, and height of a cuboid: ")
length, width, height = temp.split()
length = float(length)
width = float(width)
height = float(height)
print(length, width, height)
poly = [5, 3.2, 7.1, 0, 6.9]
x = -13

print ("Surface area of sphere = ", myMath.sphereArea(radius))
print ("Volume of sphere = ", myMath.sphereVolume(radius))
print ("Surface area of cuboid = ", myMath.cuboidArea(length, width, height))
print ("Volume of cuboid = ", myMath.cuboidVolume(length, width, height))
print (myMath.polyPrettyPrint(poly), '=', myMath.evaluatePoly(poly, x))

