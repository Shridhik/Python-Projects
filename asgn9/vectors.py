
import math
import random

class Vector:
    '''Represent mathematical vectors'''
    def __init__ (self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def as_string (self):
        return 'x={0} y={1} z={2}'.format (self.x, self.y, self.z)

    def __str__ (self):
        return self.as_string()

    def increment (self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __add__ (self, other):
        new_v = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return new_v

    def __mul__ (self, other):
        if isinstance(other, int) or isinstance (other, float):
            new_v = Vector(self.x * other, self.y * other, self.z * other)
            return new_v
        elif isinstance(other, Vector):
            return self.dotproduct(other)
        else:
            raise TypeError("can only multiply by int, float, or Vector")

    def __gt__ (self, other):
        return self.magnitude() > other.magnitude()

    def magnitude (self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def dotproduct (self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def angle (self, other = None):
        if other == None:
            other = Vector (1,0)
        return math.acos (self.dotproduct (other) / (self.magnitude() * other.magnitude()))

    def angle_degrees (self, other = None):
        return self.angle (other) * 180 / math.pi


v1 = Vector (5, 0)
v2 = Vector (2, -2)
print ("v1 is", v1)
print ("v2 is", v2)
v1 *= 2
print ("v1 is", v1)
v3 = v1 * v2
print ("v3 is", v3)
print ("v1 > v2", v1 > v2)
v4 = v2 * -5
print (sum([v1, v2, v4], Vector(0,0,0)))
vector_list = list()
for i in range (10):
    vector_list.append (Vector (random.randint (1,100), random.randint(1,100)))
vector_list.sort ()
output = '\n'.join ([str(x) for x in vector_list])
print (output)
