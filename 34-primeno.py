a=int(input("enter a number"))
for i in(2,a):
    if a%i:
         print(str(a)," is not a prime number")
         break
   
if i!=a:
     print(str(a)," is prime number")   
   