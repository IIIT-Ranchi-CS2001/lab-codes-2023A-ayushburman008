#Check For Alphanumberic
str1=input("Enter any string:")
for i in str1:
    if not (48<=ord(i)<=57 or 65<=ord(i)<=90 or 97<=ord(i)<=122):
        print("False")
        break
else:
    print("True")