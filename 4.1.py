class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __summa__(self, number):
        x1 = self.x + number.x
        y1 = self.y + number.y
        z1 = self.z + number.z
        return Vector(x1, y1, z1)

    def __difference__(self, number):
        x2 = self.x - number.x
        y2 = self.y - number.y
        z2 = self.z - number.z
        return Vector(x2, y2, z2)

    def __mult__(self, number):
        if type(number) is Vector:
            factor = self.x*number.x, self.y*number.y, self.z*number.z
            return factor
        else:
            return Vector(self.x*number,self.y*number, self.z*number)
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = v1.__summa__(v2)
printObject = '; '.join([str(v3.x), str(v3.y), str(v3.z)])
print('(' + printObject + ')')