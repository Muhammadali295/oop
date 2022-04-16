no=int(input('enter max no.:'))
for i in range(no):
    def fib(n):
        if n<=1:
            return 1
        else:
            return(fib(n-1)+fib(n-2))
    print(fib(i))