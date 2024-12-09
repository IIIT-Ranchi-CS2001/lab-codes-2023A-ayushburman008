l=list(map(int,input("Enter the list elements : ").split()))
n=len(l)
mean=sum(l)/n
ls=sorted(l)
median=ls[(n+1)//2] if n%2==0 else (ls[n//2]+ls[(n//2)+1])//2
ct=0
num=0
for i in l:
    if l.count(i)>ct:
        ct=l.count(i)
        num=i
mode=num
print(f"mean={mean},mode={mode},median={median}")