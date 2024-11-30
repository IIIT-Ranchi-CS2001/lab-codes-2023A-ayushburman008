sen=input("Enter any sentence : ")
l=sen.split()
c=0
for i in l:
    if (i==i[::-1]):
        c+=1
print(f"The no. of palindrome words in given sentence is {c}")