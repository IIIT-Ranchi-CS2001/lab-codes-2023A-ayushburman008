import pyfiglet
#Arthemetic Operations
print(pyfiglet.figlet_format('Calculator',font='doom'))
while True:
    ch=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Fraction Quotient\n5.Integer Quotient\n6.Remainder\n7.Exit\nEnter Your Choice:"))
    if(ch==7):
        break
    if(ch not in range(1,8)):
        print("Wrong Choice!Try Again")
        print("--------------")
        continue  
    a=int(input("Enter 1st No."))
    b=int(input("Enter 2nd No."))
    if(ch==1):
        print(a,"+",b,"=",a+b)
    elif(ch==2):
        print(a,"-",b,"=",a-b)
    elif(ch==3):
        print(a,"*",b,"=",a*b)
    elif(ch==4):
        print(a,"/",b,"=",a/b)
    elif(ch==5):
        print(a,"//",b,"=",a//b)
    elif(ch==6):
        print(a,"%",b,"=",a%b)
    print("--------------")