class Point:
    def __init__(self):
        self.x=(int(input('enter x-cocordinate:')))
        self.y=(int(input('enter y-cocordinate:')))
    def __str__(self):
        return f'{self.x},{self.y}'
v=Point()
print(v)
#def __add__(self, other):
        #return self.x+other.x,self.y+other.y