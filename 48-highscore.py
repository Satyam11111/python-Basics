def hiscor():
    return 799

with open("hiscore.txt",'r') as f:
    hiscore=f.read()

newscore=hiscor()


if newscore=='':
    with open("hiscore.txt","w") as f:
         f.write(str(newscore))
elif int(hiscore)<newscore:
    with open("hiscore.txt","w") as f:
        f.write(str(newscore))


      

