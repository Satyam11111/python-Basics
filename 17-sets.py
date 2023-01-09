#sets conatin uniqe values and it is unmutable

a=set()
print(type(a))         #defining empty set

a.add(1)
a.add(2)
a.add(3)
a.add(4)
print(a)

print(a.pop())    #pop the orbitely element

a.remove(4)
print(a)

print(len(a))
