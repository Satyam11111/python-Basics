class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getstatus(sel):
        print(f"The Name of train is {sel.name}")
        print(f"The seats available in the train : {sel.seats}")    

    def getfare(self):
        print(f"Fare of the train is Rs. {self.fare}")    


obj=Train("gotanjli express",90,300)
obj.getstatus()
obj.getfare()