import random

def wingame(com,player):
    
    print("********************************************************************************************")
    #decisions 
    print(f"Computer choose   :{com}")
    print(f"Player choose   :{player}")

    #if computer's choice is stone 

    if com=='st':                
        if player=='st':
            return None
        elif player=='p':
            return True
        elif player=='si':
            return False
        else:
            main("Enter valid options :")   



   #if computer's choice is paper
    elif com=='p':
        if player=='st':
            return False
        elif player=='p':
            return None
        elif player=='si':
            return True
        else:
            main("Enter valid options :") 


#if computer's choice is sissor
    elif com=='si':
        if player=='st':
            return True
        elif player=='p':
            return False
        elif player=='si':
            return None
        else:
            main("Enter valid options :")                            


 #main function
def main(string):                             

    print(string)

    #Generating computer's decision
    print("********************************************************************************************")
    print("********************************************************************************************")
    print("********************************************************************************************")
    print("com's turn : stone (st)  \t paper(p) \t sissor(si)")
    com=random.randint(1, 3)

    #assigning their names
    if com==1:
        com='st'    
    elif com==2:
        com='p'
    elif com==3:
        com='si'

    
    print("********************************************************************************************")
    #getting pleyer's decision
    player=(input("Your turn : stone (st)  \t paper(p) \t sissor(si)\t\t"))
    print("********************************************************************************************")


#generating result
    result=wingame(com,player)
   
    #declaring result
    if result==None:
        print("Match is Tie !!!")
    elif result==True:
        print("You are Win !!!") 

    else:
        print("You loose <_-_>")       

print("********************************************************************************************")
print("********************************************************************************************")
print("********************************************************************************************")
main(" ")

