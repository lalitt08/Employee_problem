import json
import csv

class Employee:
    def __init__(self, name, age, department, email, phone_no):
        self.name = name
        self.age = age
        self.department = department
        self.email = email
        self.phone_no = phone_no

    def add_employee(self):
        # Append to TXT file
        with open('employee.txt', 'a') as f1:
            f1.write(f'{self.name}, {self.age}, {self.department}, {self.email}, {self.phone_no}\n')

        # Append to CSV file
        with open('employee.csv', 'a', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerow([self.name, self.age, self.department, self.email, self.phone_no])

        # Append to JSON file
        employee_data = {
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "email": self.email,
            "phone": self.phone_no,
        }
        try:
            with open('employee.json', 'r') as f3:
                try:
                    data = json.load(f3)  # Load existing data as a list
                except json.JSONDecodeError:
                    data = []  # If file is empty or malformed, start with an empty list
        except FileNotFoundError:
            data = []  # If file does not exist, start with an empty list

        data.append(employee_data)  # Add the new employee

        with open('employee.json', 'w') as f3:
            json.dump(data, f3, indent=4)  # Write updated list back to the file

    def read_in_txt(self):
        with open('employee.txt', 'r') as f1:
            data = f1.read()
            print(data)

    def read_in_csv(self):
        with open('employee.csv', 'r') as f2:
            reader = csv.reader(f2)
            for i in reader:
                print(i)

    def read_in_json(self):
        try:
            with open('employee.json', 'r') as f3:
                data = json.load(f3)  # Load the JSON file as a list
                for employee in data:
                    print(employee)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No data found in the JSON file.")

    def update_info(self, employee_name, updated_info):
        # Update TXT file
        with open('employee.txt', "r") as f1:
            data = f1.readlines()

        with open('employee.txt', "w") as f1:
            for line in data:
                if line.startswith(employee_name + ","):
                    parts = line.strip().split(", ")
                    name = updated_info.get('name', parts[0])
                    age = updated_info.get('age', parts[1])
                    department = updated_info.get('department', parts[2])
                    email = updated_info.get('email', parts[3])
                    phone = updated_info.get('phone', parts[4])
                    f1.write(f"{name}, {age}, {department}, {email}, {phone}\n")
                else:
                    f1.write(line)


        # Update CSV file
        with open('employee.csv', "r") as f2:
            rows = list(csv.reader(f2))

        with open('employee.csv', "w", newline="") as f2:
            writer = csv.writer(f2)
            for i in rows:
                if i[0] == employee_name:
                    writer.writerow([updated_info.get('name', i[0]), updated_info.get('age', i[1]),
                                     updated_info.get('department', i[2]), updated_info.get('email', i[3]),
                                     updated_info.get('phone', i[4])])
                else:
                    writer.writerow(i)

        # Update JSON file
        try:
            with open('employee.json', "r") as f3:
                data = json.load(f3)  # Load the JSON file as a list
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  # If file doesn't exist or is malformed, start with an empty list

        for i in data:
            if i["name"] == employee_name:
                i.update(updated_info)  # Update only the fields provided

        with open('employee.json', "w") as f3:
            json.dump(data, f3, indent=4)  # Write updated list back to the file

    def delete_info(self, employee_name):
        # Delete from TXT file
        with open('employee.txt', "r") as f1:
            data = f1.readlines()

        with open('employee.txt', "w") as f1:
            for i in data:
                if not i.startswith(employee_name + ","):
                    f1.write(i)

        # Delete from CSV file
        with open('employee.csv', "r") as f2:
            rows = list(csv.reader(f2))

        with open('employee.csv', "w", newline="") as f2:
            writer = csv.writer(f2)
            for row in rows:
                if row[0] != employee_name:
                    writer.writerow(row)

        # Delete from JSON file
        try:
            with open('employee.json', "r") as f3:
                data = json.load(f3)  # Load the JSON file as a list
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  # If file doesn't exist or is malformed, start with an empty list

        data = [i for i in data if i["name"] != employee_name]  # Keep all employees except the one to delete

        with open('employee.json', "w") as f3:
            json.dump(data, f3, indent=4)  # Write updated list back to the file


def main():
    print("\nEmployee Management System")
    print("1. Add a new employee")
    print("2. Get Employee details from txt file")
    print("3. Get employee details from csv file")
    print("4. Get employee details from json file")
    print("5. Update employee details")
    print("6. Delete employee details")
    while True:
        n = input("Enter number of option: ")
        if n == "1":
            name = input("Enter employee name: ")
            age = input("Enter employee age: ")
            department = input("Enter employee department: ")
            email = input("Enter employee email: ")
            phone_no = input("Enter employee phone number: ")

            new_employee = Employee(name, age, department, email, phone_no)
            new_employee.add_employee()

        elif n == "2":
            Employee("", "", "", "", "").read_in_txt()

        elif n == "3":
            Employee("", "", "", "", "").read_in_csv()

        elif n == "4":
            Employee("", "", "", "", "").read_in_json()

        elif n == "5":
            employee_name = input("Enter the employee name to update: ")
            updated_info = {}
            if input("Update name? (y/n): ").lower() == "y":
                updated_info["name"] = input("Enter new employee name: ")
            if input("Update age? (y/n): ").lower() == "y":
                updated_info["age"] = input("Enter new employee age: ")
            if input("Update department? (y/n): ").lower() == "y":
                updated_info["department"] = input("Enter new employee department: ")
            if input("Update email? (y/n): ").lower() == "y":
                updated_info["email"] = input("Enter new employee email: ")
            if input("Update phone? (y/n): ").lower() == "y":
                updated_info["phone"] = input("Enter new employee phone number: ")

            Employee("", "", "", "", "").update_info(employee_name, updated_info)

        elif n == "6":
            employee_name = input("Enter the employee name to delete: ")
            Employee("", "", "", "", "").delete_info(employee_name)


if __name__ == '__main__':
    main()
