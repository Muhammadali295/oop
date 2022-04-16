n=int(input('enter end limit:'))
def getPrimes(n):
    if n <= 2:
        raise StopIteration
    yield 2
    for i in range(3, n, 2):
        for x in range(3, int(i**0.5)+2, 2):
            if not i % x:
                break
        else:
            yield i
for i in getPrimes(n):
    print(i)