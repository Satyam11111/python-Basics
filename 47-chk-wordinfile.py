# Write a program to read the text from a given file, “poems.txt” and find out whether it contains the word ‘twinkle’.

f=open("poem.txt","r")
s=f.read()

if 'twinkle' in s:
    print("twinkle is present")
else:
    print("twinkle is not present")    