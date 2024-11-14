import json
import csv
class Employee:
    def __init__(self, name, age, department, email, phone_no):
        self.name = name
        self.age = age
        self.department = department
        self.email = email
        self.phone_no = phone_no

    def add_Employee(self):
        with open('employee.txt','a') as f1:
            f1.write(f'{self.name}, {self.age}, {self.department}, {self.email}, {self.phone_no}\n') 

        with open('employee.csv', 'a', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerow([self.name, self.age, self.department, self.email, self.phone_no])
        
        with open('employee.json', 'a') as f3:
            employee_dict = {"name": self.name, "age": self.age, "department": self.department, "email": self.email,"phone": self.phone_no}
            json.dump(employee_dict, f3)
            f3.write("\n") 
    
    def read_in_txt(self):
        with open('employee.txt', 'r') as f1:
            data = f1.read()
            print(data) 

    def read_in_csv(self):
        with open('employee.csv','r') as f2:
            reader=csv.reader(f2)
            for i in reader:
                print(i) 

    def read_in_json(self):
        data = []
        try:
            with open('employee.json', 'r') as f3:
                for line in f3:
                    line = line.strip() 
                    if line: 
                        try:
                            employee_info = json.loads(line) 
                            data.append(employee_info)
                        except json.JSONDecodeError:
                            pass 
            print(data)
        except Exception as e:
            pass

    
    def update_info(self, employee_name, updated_info):
        #updating_info_in_textfile
        with open('employee.txt', "r") as f1:
            data = f1.readlines()
        
        with open('employee.txt', "w") as f1:
            for i in data:
                if i.startswith(employee_name + ","):
                    f1.write(f"{updated_info.name},{updated_info.age},{updated_info.department},{updated_info.email},{updated_info.phone_no}\n")
                else:
                    f1.write(i)

        # Updating_info_in_csvfile
        with open('employee.csv', "r") as f2:
            rows = list(csv.reader(f2))
        
        with open('employee.csv', "w", newline="") as f2:
            writer = csv.writer(f2)
            for i in rows:
                if i[0] == employee_name:
                    writer.writerow([updated_info.name, updated_info.age, updated_info.department, updated_info.email, updated_info.phone_no])
                else:
                    writer.writerow(i)

        #updating_info_in_jsonfile
        with open('employee.json', "r") as f3:
            data = [json.loads(line.strip()) for line in f3]
        
        for i in data:
            if i["name"] == employee_name:
                i.update(vars(updated_info))
        
        with open('employee.json', "w") as f3:
            json.dump(data, f3, indent=4) 
    
    def delete_info(self, employee_name):
        #delete from txt
        with open('employee.txt', "r") as f1:
            data = f1.readlines()

        with open('employee.txt', "w") as f1:
            for i in data:
                if not i.startswith(employee_name + ","): 
                    f1.write(i)

        # delete from csv
        with open('employee.csv', "r") as f2:
            rows = list(csv.reader(f2))

        with open('employee.csv', "w", newline="") as f2:
            writer = csv.writer(f2)
            for row in rows:
                if row[0] != employee_name: 
                    writer.writerow(row)

        # Delete from JSON file
        with open('employee.json', "r") as f3:
            data = []
            for line in f3:
                try:
                    line_data = json.loads(line.strip())
                    if line_data["name"] != employee_name:
                        data.append(line_data)
                except json.JSONDecodeError:
                # Skip malformed lines
                    pass

        # Open the JSON file again for writing
        with open('employee.json', "w") as f3:
            json.dump(data, f3, indent=4)


def main():
    print("\nEmployee Management System")
    print("1. Add a new employee")
    print("2. Get Employee details from txt file ")
    print("3. Get employee details from csv file")
    print("4. get employee details from json file")
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
            new_employee.add_Employee()

        elif n == "2":
            new_employee = Employee("", "", "", "", "")
            new_employee.read_in_txt()

        elif n == "3":
            new_employee = Employee("", "", "", "", "")
            new_employee.read_in_csv()

        elif n == "4":
            new_employee = Employee("", "", "", "", "")
            new_employee.read_in_json() 
        
        elif n == "5":
            employee_name = input("Enter the employee name to update: ")
            name = input("Enter new employee name: ")
            age = input("Enter new employee age: ")
            department = input("Enter new employee department: ")
            email = input("Enter new employee email: ")
            phone_no = input("Enter new employee phone number: ")

            updated_employee = Employee(name, age, department, email, phone_no)
            new_employee = Employee("", "", "", "", "")
            new_employee.update_info(employee_name, updated_employee)

        elif n == "6":
            employee_name = input("Enter the employee name to delete: ")
            new_employee = Employee("", "", "", "", "")
            new_employee.delete_info(employee_name)

if __name__=='__main__':
    main()

