#Count of each character of string using dictionary
str1=input("Enter a string : ")
dict1={}
for key in str1:
    if key not in dict1.keys():
        dict1[key]=1
    else:
        dict1[key]+=1
print(f"count of each elements = {dict1}")