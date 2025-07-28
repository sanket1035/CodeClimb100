students={}

n=int(input("Enter the number of Students :"))
subjects=int(input("Enter the number of Subjects:"))

for _ in range(n):
    name=input("\nEnter the Name of Student:")
    marks=[]
    
    for i in range(1,subjects+1):
        mark=int(input(f"\nEnter the Marks of Subejct{i} For {name}:"))
        marks.append(mark)

    students[name]=marks

averages={}

#Average calculation
for name,marks in students.items():
    avg = sum(marks)/len(marks)
    averages[name]=avg

#Show avg 
print("\n Student Averages:")
for name,avg in averages.items():
    print(f"{name}<-{avg:.2f}")

#Topper
topper=max(averages,key=averages.get)
print(f"Topper is {topper} with {avg:.2f}")


