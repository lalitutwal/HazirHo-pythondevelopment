def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

print("--- Student Marks System ---")

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    print("\nEnter details:")
    name = input("Enter Name: ")
    roll_no = input("Enter Roll Number: ")
    
    maths = int(input("Enter the marks of Maths: "))
    physics = int(input("Enter the marks of Physics: "))
    chemistry = int(input("Enter the marks of Chemistry: "))
    english = int(input("Enter the marks of English: "))
    computerScience = int(input("Enter the marks of Computer Science: "))
    
    total_marks = maths + physics + chemistry + english + computerScience
    percentage = (total_marks / 500) * 100
    grade = calculate_grade(percentage)
    
    print("\nResult:")
    print("Roll No:", roll_no)
    print("Name:", name)
    print("Total Marks:", total_marks, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)