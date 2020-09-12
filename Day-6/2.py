import math
class Cone:
    
    def __init__(self,R,H):
        self.R=R
        self.H=H
        
    def volume(self):
        v=3.14*(self.R**2)*(self.H)/3
        return v
    
    def surfacearea(self):
        A=3.14*(self.R)*(self.R+ math.sqrt(self.H**2 + self.R**2))
        return A
c=Cone(5,5)
print(c.volume())
print(c.surfacearea())

   
