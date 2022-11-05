companies_dict = {}

while True:
    command = input()
    if command == 'End':
        break
    company, id = command.split(' -> ')
    if company not in companies_dict.keys():
        companies_dict[company] = []
    if id not in companies_dict[company]:
        companies_dict[company].append(id)

for company_name, employees in companies_dict.items():
    print(company_name)
    print('\n'.join(f'-- {employee_id}' for employee_id in employees))




#################################### TASK CONDITION ############################
"""
                        10.	Company Users
Write a program that keeps the information about companies and their employees. 
You will be receiving company names and an employees' id until you receive 
the command "End" command. Add each employee to the given company. 
Keep in mind that a company cannot have two employees with the same id.
Print the company name and each employee's id in the following format:
"{company_name}
-- {id1}
-- {id2}
…
-- {idN}"
Input / Constraints
•	Until you receive the "End" command, you will be receiving input in the format: 
"{company_name} -> {employee_id}".
•	The input always will be valid.


____________________________________________________________________________________________
Example_01

Input
SoftUni -> AA12345
SoftUni -> BB12345
Microsoft -> CC12345
HP -> BB12345
End

Output
SoftUni
-- AA12345
-- BB12345
Microsoft
-- CC12345
HP
-- BB12345
SoftUni -> AA12345
SoftUni -> CC12344
Lenovo -> XX23456
SoftUni -> AA12345
Movement -> DD11111
End	SoftUni
-- AA12345
-- CC12344
Lenovo
-- XX23456
Movement
-- DD11111

"""
