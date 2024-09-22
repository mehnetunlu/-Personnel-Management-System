class Employee:
    def __init__(self, id, name, department, salary, days_off):
        self.id = id
        self.name = name
        self.department = department
        self.salary = float(salary)  
        self.days_off = int(days_off)  
        
    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Department: {self.department}, "
                f"Salary: {self.salary}, Days Off: {self.days_off}")

class PersonnelManagementSystem:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, id, name, department, salary, days_off):
        try:
            new_employee = Employee(id, name, department, salary, days_off)
            self.employees.append(new_employee)
            print(f"Employee {name} added successfully.")
        except ValueError as e:
            print(f"Error adding employee: {e}")
        
    def calculate_salary(self, id):
        employee = next((e for e in self.employees if e.id == id), None)
        if employee:
            print(f"{employee.name}'s salary is {employee.salary} $.")
        else:
            print("Employee not found.")
                
    def follow_permission(self, id):
        employee = next((e for e in self.employees if e.id == id), None)
        if employee:
            print(f"The remaining leave days of the employee named {employee.name} are {employee.days_off}.")
        else:
            print("Employee not found.")
                
    def show_all_employees(self):
        if not self.employees:
            print("No employees found.")
        for employee in self.employees:            
            print(employee)

if __name__ == "__main__":
    system = PersonnelManagementSystem()             

    while True:
        print("\nPersonnel Management System")
        print("1. Add employee")
        print("2. Calculate salary")
        print("3. Follow permission")
        print("4. Show all employees")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            department = input("Enter employee department: ")
            salary = input("Enter employee salary: ")
            days_off = input("Enter employee days off: ")
            system.add_employee(id, name, department, salary, days_off)
        elif choice == "2":
            id = input("Enter employee ID: ")
            system.calculate_salary(id)
        elif choice == "3":
            id = input("Enter employee ID: ")
            system.follow_permission(id)
        elif choice == "4":
            system.show_all_employees()
        elif choice == "5":
            break
        else:
            print("Invalid selection, please try again.")