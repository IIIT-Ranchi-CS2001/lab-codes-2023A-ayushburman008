#Count of occurence
str1,ch=input("Enter string and character: ").split()
ct=0
for i in str1:
    if i==ch:
        ct+=1
print(f"No. of occurences of {ch}={ct}")      