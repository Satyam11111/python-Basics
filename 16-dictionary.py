# dictionary is the pair of key and values
satyam ={
    "boy":"satyam",
    "age": 15,
    "time":20 ,
    'sb':{
        'sbb':"mich"           #we can add list in an danother dictionary in dictionary
    },
    'ss':(1,2,3,4)
}

# print(satyam)
# print(satyam.keys())     #it prints the all key of dictionary satyam

# print(satyam.items())     it prints the all values of directory

# gaurav={
#     'a':[1234,233]
# }
# satyam.update(gaurav)

# print(satyam)


print(satyam['sb']['sbb'])
print(satyam['age'])
