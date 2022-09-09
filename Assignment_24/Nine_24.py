# Write a python program to create a school class and 3 instance variables and 1 class variable

class School:
    school_name = "ST. Paul's School"
    
    def __init__(self, name, std, rollno):
        self.name = name
        self.std = std
        self.rollno = rollno
        
student = School('Arya', 8, 33)

print(f'Name {student.name}')
print(f'Standard {student.std}')
print(f'Roll number {student.rollno}')
print(f'School {student.school_name}')
