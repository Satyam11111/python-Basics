class c2dvect:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"icap= {self.icap} jcap= {self.jcap}"


class c3dvect(c2dvect):
    def __init__(self,i,j,k):
        super().__init__(i, j)
        self.kcap=k

    def __str__(self):
        return f"icap= {self.icap} jcap= {self.jcap} kcap= {self.kcap}"


vectobj=c3dvect(3, 3, 4)        
print(vectobj)