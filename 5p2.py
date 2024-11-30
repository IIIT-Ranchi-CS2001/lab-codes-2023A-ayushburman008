#Equation of Straight line with 2 cartesian points
from math import sqrt
t1=tuple(map(int,input("Enter x y of first tuple : ").split()))
t2=tuple(map(int,input("Enter x y of   other tuple : ").split()))
print(f"Straight line Eqn :- Y={(t1[0]-t2[0])/(t1[1]-t2[1])}X + {(((t1[0]-t2[0])/(t1[1]-t2[1]))*t1[0])+t1[1]}")