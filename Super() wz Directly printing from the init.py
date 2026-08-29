class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person initialized")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        # Initialize the Person part first
        super().__init__(name, age)  # Python 3 syntax
        # Then add Employee-specific initialization
        self.employee_id = employee_id
        print("Employee initialized")

emp = Employee("Alice", 30, "E123")