import time
t=int(input('lenght of coundown in seconds:'))
while t:
    mins=t//60
    secs=t%60
    timer='{:02d}:{:02d}'.format(mins,secs)
    print(timer,end="\r")
    time.sleep(1)
    t-=1
