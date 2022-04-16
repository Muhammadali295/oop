x=int(input('enter the end limit:'))
for i in range(x):
    def fib(n):
        if n<=1:
           yield 1
        else:
           yield (x-1)+(x-2)
    print(fib(i))
