class complex:
    def __init__(self,r,i):
        self.real=r
        self.img=i

    def __add__(self,c):
        return complex(self.real+c.real, self.img +c.img)


    def __mul__(self,c):
        return complex(self.real*c.real, self.img *c.img)  

    def __str__(self):
        return f"{self.real} + {self.img}i"   


obj1=complex(5, 2)             
obj2=complex(7, 4)
print(obj1+obj2)
print(obj1*obj2)