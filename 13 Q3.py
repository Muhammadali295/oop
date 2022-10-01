class Circle:
    def __init__(self,r):
        self.r=r
    def __lt__(self, other):
        if self.r<other.r:
            return 'c1 is less'
    def __gt__(self, other):
        if self.r>other.r:
            return 'c1 is greater'
c1=Circle(7)
c2=Circle(9)
print(c1<c2 or c1>c2)