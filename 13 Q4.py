class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #def __add__(self, other):
        #return self.x+other.x,self.y+other.y
    def __lt__(self, other):
        a=self.x<other.x
        b=self.y<other.y
        if a and b:
            return True
        else:
            return False
    def __gt__(self, other):
        a=self.x>other.x
        b=self.y>other.y
        if a and b:
            return True
        else:
            return False
p1=Point(40,6)
p2=Point(10,56)
#print('point is:',p1+p2)
if p1<p2:
    print(p1 < p2)
else:
    print(p1>p2)