# Initialize an empty list to store students' data
students_data = []

# Step a: Ask for the number of students
num_students = int(input("Enter the number of students in your class: "))

# Step b and c: Gather each student's data and calculate the CA grade
for _ in range(num_students):
    name = input("Enter student name: ")

    # Ensure input is within required ranges
    while True:
        activities_grade = float(input("Enter the Marked Activities grade (between 0 and 25): "))
        if 0 <= activities_grade <= 25:
            break
        print("Invalid grade. Please enter a value between 0 and 25.")

    while True:
        attendance_grade = float(input("Enter the Attendance grade (between 0 and 5): "))
        if 0 <= attendance_grade <= 5:
            break
        print("Invalid grade. Please enter a value between 0 and 5.")

    while True:
        tma_grade = float(input("Enter the TMA grade (between 0 and 20): "))
        if 0 <= tma_grade <= 20:
            break
        print("Invalid grade. Please enter a value between 0 and 20.")

    # Calculate the CA grade as the sum of the three grades
    ca_grade = activities_grade + attendance_grade + tma_grade

    # Store all student information in a single list entry
    students_data.extend([name, activities_grade, attendance_grade, tma_grade, ca_grade])

# Step d: Print the revised list of all students and their grades
print("\nThe list of students and their grades:")
print(students_data)

# Step e: Count students with CA grade < 15 and Step f: Display their names and CA grade
failing_students = [(students_data[i], students_data[i + 4]) for i in range(0, len(students_data), 5) if
                    students_data[i + 4] < 15]
print("\nThe number of students who failed the CA is:", len(failing_students))

# Print the names and CA grades of failing students
if failing_students:
    print("\nName and CA of the failing student(s):")
    for student_name, ca_grade in failing_students:
        print(student_name, ca_grade)
else:
    print("No students failed.")
