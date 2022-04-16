def out_circle(r):
    print('area of outer circle:',3.142*r**2)
    r2=int(input('enter value of Inradius:'))
    if r2<r:
        def in_circle(r1):
            print('circumference:',2*3.14*r)
        in_circle(r2)
out_circle(12)
