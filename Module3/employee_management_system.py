print("--- Employee Management System ---")


high_salary_employees = ["101"]

employee_database = {
    "101": {
        "full_name": "Amit Kumar",
        "job_title": "Software Developer",
        "salary_amount": 60000,
    },
    "102": {
        "full_name": "Rahul Sharma",
        "job_title": "UI UX Designer",
        "salary_amount": 50000,
    },
}


def add_employee():
    new_employees_adding = int(input("\nHow many employees do you want to add? "))

    for count in range(new_employees_adding):
        print("\nEnter New Employee Details:")
        employee_id = input("Enter Employee ID: ")
        full_name = input("Enter Full Name: ")
        job_title = input("Enter Job Title: ")
        salary_amount = int(input("Enter Salary Amount: "))

        # Adding data to the dictionary
        employee_database[employee_id] = {
            "full_name": full_name,
            "job_title": job_title,
            "salary_amount": salary_amount,
        }

        # Checking if salary is high to add to the list
        if salary_amount >= 80000:
            high_salary_employees.append(employee_id)


def display_employee():
    print("\n--- Current Employee List ---")
    for employee_id in employee_database:
        single_employee_data = employee_database[employee_id]
        print("ID:", employee_id)
        print("Name:", single_employee_data["full_name"])
        print("Title:", single_employee_data["job_title"])
        print("Salary:", single_employee_data["salary_amount"])
        print("-" * 20)

    print("High Salary Employee IDs (List):", high_salary_employees)


choice = int(input("add employees / display employees (1/2): "))

if choice == 1:
    add_employee()
if choice == 2:
    display_employee()
else:
    print("not a valid input\n")
