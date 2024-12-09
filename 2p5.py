#Quadratic Roots Finder
from math import sqrt
a,b,c=map(int,input("Enter three space separated coefficients").split())
d=b**2-4*a*c
if d==0:
    print(f"The eqn has one real and repeated root :-{(-b)/(2*a)}")
elif d>0:
    print(f"The eqn has two real and distinct root :-{((-b)+sqrt(d))/(2*a)} and {(-b-sqrt(d))/(2*a)}")
else:
    print(f"The eqn has two complex root whose real part :-{(-b)/(2*a)} and imaginary part :-{(sqrt(d))/(2*a)}")

    