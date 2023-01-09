
class Calculator:
    def square(self,num):
        return num*num

    def cube(self,num):
        return num*num*num

    def sqart(self,num):
        return num**0.5  

    @staticmethod
    def greet():
        print("hello ji")       



num1=Calculator()
num2=Calculator()

print(f"{num1.greet()}The number is 5 = square= {num1.square(5)}  cube= {num2.cube(5)}  square root= {num1.sqart(25)} ")

