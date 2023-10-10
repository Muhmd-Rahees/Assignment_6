# 👉 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects


import json

class Employee:

    def __init__(self, name, dob, height, city, state):

        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open(r"C:\Users\user\Documents\DS140823\Assignment_6\employee.json", 'r') as file:

    data = json.load(file)
    

    employees = []
for employee_data in data:
    employee = Employee(
        employee_data['Name'],
        employee_data['DOB'],
        employee_data['Height'],
        employee_data['City'],
        employee_data['State']
    )
    employees.append(employee)
   


for employee in employees:
    print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")