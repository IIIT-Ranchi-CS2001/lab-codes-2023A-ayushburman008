#Multiplication Tabel Untill Limit
num,lim=map(int,input("Enter the no. and limit space separated: ").split())
i=1
while i<=lim:
    print(f"{num} x {i} = {num*i}")
    i+=1