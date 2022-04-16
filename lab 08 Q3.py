r1=int(input('enter the starting range value?'))
r2=int(input('enter the ending range value?'))
num=r1+1
count=0
while num<r2:
    res=num%2
    if (num%2)>0:
        count+=1
    num+=1
print('odd count:%d'%count)