x=5
s=0

def rec(x):
    if x==0:
        return 0
    s=x+rec(x-1)
    return s


print(rec(x))    