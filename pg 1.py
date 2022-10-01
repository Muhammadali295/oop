import time
class Time:
    def __init__(self,h=0,m=0,s=0):
        self.hour=h
        self.minute=m
        self.second=s
    def add_time(self,t):
        h=t.hours
        m=t.minutes
        s=t.seconds
        if type(t)==time:
          if self.second>=60:
            self.minute +=self.second//60
            self.second%=60
          if self.minute>60:
            self.hour+=self.
            self.m-=60
        Time.print_time(self)
    def print_time(self):
        print(self.h,':',self.m,':',self.s)

t1=Time(18,19,20)
t2=Time(2,19,4)
t1.add_time(t2)

