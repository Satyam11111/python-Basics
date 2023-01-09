with open("donkey.txt","r") as f:
    content1=f.read()


with open("copyfile.txt","r") as f:
    content2=f.read()


if(content1==content2):
    print("both file is identical")    
else:
    print("both file is not identical")    
