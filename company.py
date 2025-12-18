class Company:
    class Employee:
        def __init__(self, emp_id, name, position, salary):
            self.emp_id = emp_id
            self.name = name
            self.position = position
            self.salary = salary

        def display_info(self):
            print(f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}")


    class CompanyInfo:
        def __init__(self, name, location):
            self.name = name
            self.location = location
            self.employees = []

        def add_employee(self, emp_id, name, position, salary):
            employee = Company.Employee(emp_id, name, position, salary)
            self.employees.append(employee)
            print(f"Employee {name} added successfully!")

        def remove_employee(self, emp_id):
            self.employees = [e for e in self.employees if e.emp_id != emp_id]
            print(f"Employee with ID {emp_id} removed!")

        def search_employee(self, emp_id):
            for emp in self.employees:
                if emp.emp_id == emp_id:
                    return emp
            return None

        def show_all_employees(self):
            if not self.employees:
                print("No employees found!")
                return
            for emp in self.employees:
                emp.display_info()

        def display_info(self):
            print(f"Company Name: {self.name}")
            print(f"Location: {self.location}")
            print(f"Employee Count: {len(self.employees)}")


# Dynamic input
company = Company.CompanyInfo(input("Enter company name: "), input("Enter location: "))

while True:
    choice = input("\n1. Add Employee\n2. Show All Employees\n3. Search Employee\n4. Remove Employee\n5. Exit\nEnter choice: ")
    
    if choice == "1":
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        position = input("Enter position: ")
        salary = int(input("Enter salary: "))
        company.add_employee(emp_id, name, position, salary)
    
    elif choice == "2":
        company.display_info()
        print("\nEmployees:")
        company.show_all_employees()
    
    elif choice == "3":
        emp_id = int(input("Enter employee ID to search: "))
        emp = company.search_employee(emp_id)
        if emp:
            emp.display_info()
        else:
            print("Employee not found!")
    
    elif choice == "4":
        emp_id = int(input("Enter employee ID to remove: "))
        company.remove_employee(emp_id)
    
    elif choice == "5":
        break
    
    else:
        print("Invalid choice!")
