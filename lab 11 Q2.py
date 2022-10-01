def Smart_division():
    try:
        no1=int(input('enter numinator:'))
        no2=int(input('enter denomenator:'))
        a=no1/no2
    except ZeroDivisionError as d:
        print(d)
    except TypeError as t:
        print(t)
    else:
        print(a)
Smart_division()