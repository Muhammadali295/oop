class Vector:
    def __init__(self):
        self.x=(int(input('enter x-cocordinate:')))
        self.y=(int(input('enter y-cocordinate:')))
    def __str__(self):
        return f'{self.x}i+{self.y}j'
v=Vector()
print(v)