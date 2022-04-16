y=int(input('enter end limit:'))
def fib(num):
    a,b=0,1
    for i in range(num):
        yield a
        a,b=b,a+b
for i in fib(y):
    print(i)