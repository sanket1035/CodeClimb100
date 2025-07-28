'''🔥 Question 1: Student Marks Analyzer
🧾 Topics used: Input, Loops, Lists, Dict, Functions
📄 Task: Write a Python program that:
Takes input of 5 students and their marks in 3 subjects each.
Stores data in a dictionary like this:

{
  "Aman": [80, 90, 70],
  "Priya": [60, 65, 72]
}

Then:

Calculates average marks per student
Finds the student with highest average
Prints all students with their average
🔁 Bonus: Use list comprehension to calculate average'''

# Actual code
students = {}

n = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

for _ in range(n):
    name = input("\nEnter student name: ")
    marks = []

    for i in range(1, subjects + 1):
        mark = int(input(f"Enter marks in subject {i} for {name}: "))
        marks.append(mark)

    students[name] = marks

# Calculate averages
averages = {}
for name, marks in students.items():
    avg=sum(marks) / len(marks)
    averages[name] = avg

# Print student averages
print("\n Student Averages:")
for name, avg in averages.items():
    print(f"{name} → {avg:.2f}")

# Find topper
topper = max(averages, key=averages.get)
print(f"\n Topper is {topper} with {averages[topper]:.2f} average marks.")




    
    



    
    

