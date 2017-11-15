class Vector:
    def as_string (self):
        return 'x={0} y={1}'.format (self.x,self.y)

    def add_vector(self, other):
        new_v = Vector()
        new_v.x = self.x + other.x
        new_v.y = self.y + other.y
        return new_v


    def increment (self,other):
        self.x += other.x
        self.y += other.y



def make_vector (x,y):
    v = Vector()
    v.x = x
    v.y = y
    return v



    v = make_vector (3,4)
    print (v.as_string())
    v1 = make_vector (4,5)
    print(v1.as_string())
    v2 = v1.add_vector(v)
    print (v2.as_string(()))
