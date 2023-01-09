with open("donkey.txt","r") as f:
    content=f.read()

with open("copyfile.txt","w") as f:
    f.write(content)    