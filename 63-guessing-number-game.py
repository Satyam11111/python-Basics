import random
userguesses=0
userguess=None
randomnumber=random.randint(1, 100)
while(userguess!=randomnumber):
    print("****************************************************************************")
   
    userguess=int(input("Enter the number !\n"))
    if(userguess==randomnumber):
        print("You guss right !")
        userguesses+=1
    else:
        userguesses+=1
        if(userguess<randomnumber):
            print("Enter bigger number !")
            print("****************************************************************************")
        else:
            print("Enter smaller number")
            print("****************************************************************************")

with open("hiscore1.txt") as f:
    hiscore=int(f.read())

with open("hiscore1.txt","w")as f:
    if(hiscore>userguesses):
        f.write(str(userguesses))    
print(f"You guess in {userguesses} guesses !")            

