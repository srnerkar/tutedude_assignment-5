''' This program will create student with marks and will search the student name and return with marks.
 If name not present then return error message'''

# default directory
student_marks = {
    "Anil": 60,
    "Prakhar": 90,
    "Ajit": 54,
    "Rajesh": 82
}

# user input
name = input("Enter the student's name : ").capitalize()

if student_marks.get(name):
    print("{}'s marks: {}".format(name, student_marks[name]))
else:
    print("Student not found.")
