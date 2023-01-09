with open("donkey.txt","r") as f:
    flstring=f.read()
    flstring=flstring.replace("donkey","#######")
    

# flstring.replace("donkey","#######")

with open("donkey.txt","w") as f:
#     flstring.replace("donkey","#######")
    f.write(flstring)