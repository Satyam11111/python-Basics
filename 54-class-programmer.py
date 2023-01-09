class Programmer:
    company:"microsoft"
    def getdata(self):
        print(f"name= {self.name} age= {self.age} company= {self.company}")

emp1=Programmer()
emp2=Programmer()
emp2.name="gaurav"
emp2.age=19
emp1.name="satyam"
emp1.age=18

emp1.getdata()
# print(emp1.name)
# print(emp1.age)
# print(emp1.company)

