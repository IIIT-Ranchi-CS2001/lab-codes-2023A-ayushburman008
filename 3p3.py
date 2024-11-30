#Fibonacci Series(0,1,1,2,3,5,8,13,.....)
a=0
b=1
i=1
n=int(input("Enter the no. of terms: "))
while i<=n:
    if i==1:
        print("0",end=",")
        i+=1
    if i==2:
        print("1",end=",")
        i+=1
    S=a+b
    a=b
    b=S
    print(S,end=",")
    i+=1