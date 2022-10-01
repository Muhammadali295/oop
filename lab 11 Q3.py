def factorial():
    try:
        a=int(input('enter a no:'))
        assert a>0, f'{a} is not greater than zero'
        for i in range(1,a):
            a=a*i
        print('factorial of no is:',a)
    except TypeError as t:
        print(t)
    except AssertionError as e:
        print(e)
factorial()