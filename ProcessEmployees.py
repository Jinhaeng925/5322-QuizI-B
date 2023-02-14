'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
'''

import csv

#open the file
emp_data = open("employee_data.csv", "r")

# using the csv library, create a csv object the delimiter ',' tells the program how the columns are seperated
emp_data_file = csv.reader(emp_data, delimiter=",")

# skip the first line in the csv file
next(emp_data_file)

#create an empty dictionary
emp_newSalary_dic = {}

#create an dictionary input counter
input_count = 0

# increase in salary 
increase_in_salary = 1.1

# Create a variable to track how much bonus funds are required for the reward
bonus_fund = 0

# Total Current Salary
total_cur = 0
# Total New Salary
total_new = 0

#use a loop to iterate through the csv file
for record in emp_data_file:
    employeeID = record[0]
    employeeFullName = record[1] + " " + record[2]
    department = record[3]
    title = record[4]
    salary = float(record[5])
    hire_date = record[6]
    birth_date = record[7]
    gender = record[8]
    clearance = record[9]

    #check if the employee fits the search criteria, and add to the emp_dic
    if department == "Marketing" and clearance == "TS":
        old_salary = salary
        new_salary = salary * increase_in_salary
        
        emp_newSalary_dic[input_count] = {
            "Full Name": employeeFullName,
            "New Salary": new_salary
        }

        input_count = input_count + 1

for key, value in emp_newSalary_dic["Full Name"].items():
    print(f"Employee Name: {key} Current Salary: ${(value/increase_in_salary):,.2f}")
    total_cur = total_cur + float((value/increase_in_salary),2)

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per image
for key, value in emp_newSalary_dic["Full Name"].items():
    print(f"Employee Name: {key} New Salary: ${value:,.2f}")
    total_new = total_new + float(value,2)
        
print()
print('=========================================')
print()

#print out the total difference between the old salary and the new salary as per image.
bonus_fund = total_new - total_cur

print(f"Total increase in salary: ${bonus_fund:,.2f}")
        
    
