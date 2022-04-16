import math
class Point:
   def reset(self):
       self.move(0,0)
   def move(self, x, y):
       self.x = x
       self.y = y
   def calculate_distance(self,other_point):
       return math.sqrt((self.x -other_point.x)*2 +(self.y -other_point.y)*2)