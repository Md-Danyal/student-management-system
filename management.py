from student import Student

class StudentManagement:
    def __init__(self):
        self.std = {}

    # REUSABLE METHODS:--
    def empty_dic(self):
        if not self.std:
            print("No student records found.")
            return True
        return False
    
    def std_data(self,std_view):
        print("\n++ Student Found ++\n")
        print("-Current details-")
        std_view.display()

    # EXEPTION HANDLING

    def valid_int(self,number):
        while True:
            try:
                value = int(input(number))
                if value < 0:
                    raise ValueError
                return value
            except ValueError:
                print("Invalid input! Please enter a valid number")

    # STARTS FROM HERE:--
    # 1
    def add_std(self):
        while True:
            print("---Enter Std details---")
            std_id = self.valid_int("Enter Student ID : ")
            if std_id in self.std:
                print("ID already exists! Try another ID.")
                continue

            name = input("Enter std name : ")
            age = self.valid_int("Enter Student Age : ")
            self.std[std_id] = Student(std_id,name,age)

            cont = input("Do you want to add another student? (y/n): ").lower()
            if cont != 'y':
                break
            print("-"*30)

    # 2
    def view_std(self):
        if self.empty_dic():
            return
    
        for student in self.std.values():
            student.display()

    # 3
    def search_std(self):
        if self.empty_dic():
            return

        search_id = self.valid_int("Enter student ID to search: ")
        if search_id in self.std:
            self.std_data(self.std[search_id])
        else:
            print("Student not found.")

    # 4
    def update_std(self):
        if self.empty_dic():
            return

        upd_id = self.valid_int("Enter student ID to update: ")
    
        if upd_id in self.std:
            self.std_data(self.std[upd_id])
            new_name = input("Enter new name : ")
            new_age = self.valid_int("Enter new age : ")
            self.std[upd_id].std_name = new_name
            self.std[upd_id].std_age = self.std[upd_id].validate_age(new_age)

        else:
            print("Student not found")

    # 5
    def delete_std(self):
        if self.empty_dic():
            return

        delete_id = self.valid_int("Enter student Id to delete: ")
    
        if delete_id in self.std:
            self.std_data(self.std[delete_id])
            del self.std[delete_id]
            print(f"Student with ID {delete_id} has been deleted.")
        else:
            print("Student not found.")