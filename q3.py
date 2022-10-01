import time
class Speedy:
    def __init__(self,c=0.1):
        self.clock_rate=c
    def no_of_cycles(self,n):
        self.no_of_cycles=n
    def find_time(self):
        return (self.clock_rate/self.no_of_cycles)*10**-9

class Memorized:
    def __init__(self,type:str,size=0):
        self.type=type
        self.size=size
    def sizemb(self):
        self.sizemb=self.size/1024
    def printmemory(self):
        print('memorytype:',self.type,'capacity:',self.size,self.sizemb,'size in mb:',self.sizemb,'size in mb:',self.size)

class Computer(Speedy,Memorized):
    def __init__(self):
        super.__init__(c,type,size)