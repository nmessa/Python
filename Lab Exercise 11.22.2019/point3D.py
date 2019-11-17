#3D Point class definition
#Author nmessa
#Date: 11/22/2019
#This class may be used anyplace that requires a Point
#with coordinates (x, y, z)

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' \
               + str(self.z) + ')'



