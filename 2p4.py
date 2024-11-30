#Grade Calculator
name,roll,marks=input("Enter Name Roll and Marks seperated by space").split()
marks=int(marks)
if (marks<50):
    grade=0
    rem="Fail"
elif (marks<60): 
    grade=6
    rem="Pass"
elif (marks<70): 
    grade=7
    rem="Average"
elif (marks<80): 
    grade=8
    rem="Good"
elif (marks<90): 
    grade=9
    rem="Very Good"
else: 
    grade=10
    rem="Outstanding" 
print(f"Name:-{name}\nRoll No.:-{roll}\nMarks:-{marks}\nGradePoint:-{grade}\nRemarks:-{rem}")