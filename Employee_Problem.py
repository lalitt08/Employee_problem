import json
import csv
class Employee:
    def __init__(self, name, age, department, email, phone_no):
        self.name = name
        self.age = age
        self.department = department
        self.email = email
        self.phone_no = phone_no

    def add_in_file(self):
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
        with open('employee.json', 'r') as f3:
            for i in f3:
                employee_info = json.loads(i.strip())
                print(employee_info)  
    
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

new_employee = Employee("lalit sangore", 22, "IT", "sangorelalit@gmail.com", "123-456-7890")
updated_employee = Employee("lalit sangore", 31, "HR", "sangorelalit@gmail.com", "987-654-3210")
new_employee.update_info("lalit sangore", updated_employee)