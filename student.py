from base import Person

class Student(Person):
    def __init__(self, std_id, name, age):
        self.std_id = std_id
        self.std_name = name
        self.std_age = self.validate_age(age)

    def validate_age(self, age):
        if age < 18:
            print("Age is not valid")
            return None
        else:
            return age
        
    def display(self):

        print("="*40)
        print(f"{'ID':<10} {'NAME':<15} {'AGE':<5}")
        
        print(f"{self.std_id:<10} {self.std_name:<15} {self.std_age:<5}")
        print("="*40)