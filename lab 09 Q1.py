print('calculator')
def calculator():
    def addition():
        total=0
        n=int(input('enter the max no.s:'))
        for i in range(n):
            no=int(input('please enter a no.'))
            total=total+no
        print('total no.s are:',total)
    def subtraction():
        x1=int(input('enter 1st no:'))
        x2=int(input('enter 2nd no:'))
        print('answer:',x1-x2)
    def multiplication():
        x1 = int(input('enter 1st no:'))
        x2 = int(input('enter 2nd no:'))
        print('answer:', x1*x2)
    def division():
        x1 = int(input('enter 1st no:'))
        x2 = int(input('enter 2nd no:'))
        print('answer:', x1/x2)
    print('select 1 of following:addition,subtraction,multiplication,division')
    x=input('enter:')
    if x=='addition':
       addition()
    if x=='subtraction':
        subtraction()
    if x=='multiplication':
        multiplication()
    if x=='division':
        division()
calculator()