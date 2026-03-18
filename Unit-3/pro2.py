class Student:
    def __init__(self):
        # Initializing attributes to None or empty strings
        self.roll_no = None
        self.name = None
        self.age = None
        self.gender = None

    def add_student(self):
        """Method to collect student details from user input"""
        print("--- Enter Student Details ---")
        self.roll_no = input("Enter Roll No: ")
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.gender = input("Enter Gender: ")
        print("Student data added successfully!\n")

    def display_student(self):
        """Method to display the stored student details"""
        print("--- Student Record ---")
        if self.name is None:
            print("No data available. Please add a student first.")
        else:
            print(f"Roll No : {self.roll_no}")
            print(f"Name    : {self.name}")
            print(f"Age     : {self.age}")
            print(f"Gender  : {self.gender}")
        print("\n")




student_obj = Student()


student_obj.add_student()


student_obj.display_student()