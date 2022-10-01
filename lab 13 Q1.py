class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return self.x+other.x,self.y+other.y
p1=Point(4,5)
p2=Point(10,56)
print('point is:',p1+p2)