#Euclidean Distance B/w two 3D points
from math import sqrt
t1=tuple(map(int,input("Enter x y z of first tuple : ").split()))
t2=tuple(map(int,input("Enter x y z of other tuple : ").split()))
dist=sqrt(pow(t2[0]-t1[0],2)+pow(t2[1]-t1[1],2)+pow(t2[2]-t1[2],2))
print(f"The Euclidean Distance b/w points = {dist}")