class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __add__(self,c):
        return f"{self.i+c.i}i + {self.j+c.j}j + {self.k+c.k}k"  

#   dot product
    def __mul__(self,c):
        sum=0
        sum= (self.i*c.i) + (self.j*c.j) + (self.k*c.k)     
        return sum 

    def __str__(self):
        return  f"{self.i}i + {self.j}j + {self.k}k"

    def __len__(self):
        return     




vc =vector(1, 3, 4)   
vc2=vector(4, 4, 4)
print(vc*vc2)