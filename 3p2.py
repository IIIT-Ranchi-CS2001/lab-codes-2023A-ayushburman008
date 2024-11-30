#Sum of digits of a number
n=int(input("Enter the no."))
temp=n
Sum=0
while temp!=0:
    r=temp%10
    temp=temp//10
    Sum=Sum+r
print(f"No.={n}     Sum Of Digits={Sum}")