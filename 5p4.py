#Create list of tuples with and without zip
Cname=input("Enter Customer Names Space separated : ").split()
Cid=list(map(int,input("Enter Customer Id's Spaces separated : ").split()))
Shp=input("Enter Shoping Points Spaces separated : ").split()
#with zip
Lotz=list(zip(Cname,Cid,Shp))
print(Lotz)
#without zip
Lotwz=[]
for i in range(len(Cname)):
    Lotwz.append((Cname[i],Cid[i],Shp[i]))
print(Lotwz)