student_name = str(input("Enter Student Name: "))
student_roll_no = input("Enter Student Roll No: ")
sub_1 = int(input("Web Development: "))
sub_2 = int(input("Data Mining: "))
sub_3 = int(input("Artificial Intelligence: "))

total_marks = 300

obt_marks = sub_1 + sub_2 + sub_3
#print("Obtained Marks: ", obt_marks)

percentage = (obt_marks / total_marks) * 100
#print("Percentage: ", percentage)

Grade = ""

if percentage >= 80:
    Grade = "A+"
elif percentage >= 70:
    Grade = "A"
elif percentage >= 60:
    Grade = "B"
elif percentage >= 50:
    Grade = "C"
elif percentage >= 40:
    Grade = "D"
else:
    Grade = "Fail"

print("\n--------------------------------")
print("      Student Report Card       ")
print("--------------------------------\n")
print(f"Student Name   : {student_name}")
print(f"Student Roll No: {student_roll_no}")
print("\n--------------------------------\n")
print(" Subject                   Marks")
print("--------------------------------\n")
print(f"Web Development             {sub_1}")
print(f"Data Mining                 {sub_2}")
print(f"Artificial Intelligence     {sub_3}")
print("\n--------------------------------\n")
print("Total Marks: 300")
print("--------------------------------\n")
print(f"Obtained Marks: {obt_marks} out of {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {Grade}")
