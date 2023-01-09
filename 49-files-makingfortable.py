def table(a):
    i=1
    with open(f"multiplication_table_of_{a}.txt","w") as f:
        while i<=10:
            f.write(f"{a} x {i} = {a*i}\n")
            i+=1
      



for j in range(2,20):
    table(j)