# COMP2152 Assignment 01
# Made by Ali Al Aoraebi
# Student number: 101386021
# Lab Instructor: Michael Murphy

def print_menu():
    print("----------------------------")
    print("| 1. Create Employee       |")
    print("| 2. Create Item           |")
    print("| 3. Make Purchase         |")
    print("| 4. All Employee Summary  |")
    print("| 5. Exit                  |")
    print("----------------------------")


def get_menu_option():
    user_input = input("Select menu option: ")
    if user_input == "1":
        get_employee_info()
    elif user_input == "2":
        get_item_info()
    elif user_input == "3":
        purchase_items(item_list, employee_list)
    elif user_input == "4":
        get_employee_summary(employee_list)
    elif user_input == "5":
        exit()
    else:
        print("Enter valid option!")


employee_list = []


def get_employee_info():
    global employee_list

    while True:
        emp_id = input("Enter employee ID: ")
        if emp_id == "NO":
            employee_discount_program()

        # Validate if the employee ID is integer
        if not emp_id.isnumeric():
            print("Error: employee ID is not a number.")
            continue

        # Validate if the employee ID is unique
        emp_id = int(emp_id)
        id_list = [employee[0] for employee in employee_list]
        if emp_id in id_list:
            print("Error: employee ID must be unique.")
            continue

        emp_name = input("Enter employee name: ")
        # Validate if employee name is a string
        while not emp_name.isalpha():
            print("Error: employee name is not a name.")
            emp_name = input("Enter employee name: ")

        emp_type = input("Enter employee type (hourly or manager): ")
        while emp_type not in ["hourly", "manager"]:
            print("Error: employee type must be either 'hourly' or 'manager.'")
            emp_type = input("Enter employee type (hourly or manager): ")

        years_worked = input("Enter years worked: ")
        # Validates if the input is an integer
        while not years_worked.isnumeric():
            print("Error: years worked must be in numbers.")
            years_worked = input("Enter years worked: ")

        total_purchased = 0
        total_discount = 0

        emp_discount = input("Enter employee discount number: ")

        # Validating if user inputs number for employee discount number
        if not emp_discount.isnumeric():
            print("Error: employee discount number must be a number.")
            emp_discount = input("Enter employee discount number: ")

        # Validating if the employee discount number is unique
        emp_discount = int(emp_discount)
        discount_list = [employee[6] for employee in employee_list]
        if emp_discount in discount_list:
            print("Error: employee discount number must be unique.")
            continue

        employee = [int(emp_id), emp_name, emp_type, int(years_worked), total_purchased, total_discount,
                    int(emp_discount)]
        employee_list.append(employee)
    return employee_list


item_list = []


def get_item_info():
    global item_list

    while True:
        item_number = input("Enter item number: ")
        if item_number == "NO":
            employee_discount_program()

        # Validating if item number is integer
        if not item_number.isnumeric():
            print("Error: item number is not a number.")
            continue

        # Validating if item number is unique
        item_number = int(item_number)
        item_number_list = [item[0] for item in item_list]
        if item_number in item_number_list:
            print("Error: item number must be unique.")
            continue

        item_name = input("Enter item name: ")
        # Validating if item name is a string
        while not item_name.isalpha():
            print("Error: item name is not a name.")
            item_name = input("Enter item name: ")

        item_cost = input("Enter item cost: ")
        # Validating if item cost is a number
        while not item_cost.isnumeric():
            print("Error: item cost must be in number.")
            item_cost = input("Enter item cost: ")

        item = [int(item_number), item_name, int(item_cost)]
        item_list.append(item)
    return item_list


def purchase_items(item_list, employee_list):
    item_menu = ["Item Number", "Item Name", "Item Cost"]
    print(f"{item_menu[0]:<10} | {item_menu[1]:<11}| {item_menu[2]}")

    for item in item_list:
        print(f"{item[0]:<11} | {item[1]:<11}| ${item[2]}")

    while True:
        emp_discount_num = input("Enter employee discount number: ")
        if emp_discount_num == "NO":
            ans = input("Another purchase? ")
            if ans == "Y":
                continue
            elif ans == "N":
                get_employee_summary(employee_list)

        emp = None
        for i in range(len(employee_list)):
            if int(employee_list[i][6]) == int(emp_discount_num):
                emp = employee_list[i]
                break

        if emp is None:
            print("Error: employee not found.")
            continue

        # Validating if employee reached max discount limit
        if emp[4] >= 200:
            print("Error: Discount limit reached.")
            continue

        item_num = input("Enter item number: ")
        item = None
        for i in range(len(item_list)):
            if int(item_list[i][0]) == int(item_num):
                item = item_list[i]
                break

        if not item:
            print("Error: item not found.")
            continue

        # Calculating the discount
        discount = 0
        if emp[2] == "hourly":
            discount = emp[3] * 0.02
        elif emp[2] == "manager":
            discount = (emp[3] * 0.02) + 0.1

        if discount > 0.1:
            discount = 0.1

        if emp[4] + discount > 200:
            discount = 200 - emp[4]

        total_cost = item[2] - (item[2] * discount)

        emp[4] += discount
        emp[5] += total_cost

        # display purchase detail
        print(f"Item Name: {item[1]}")
        print(f"Item Cost: {item[2]}")
        print(f"Discount: {discount * 100:.2f}%")
        print(f"Total Cost: ${total_cost}")
        print(f"Employee Name: {emp[1]}")
        print(f"Total Purchased: ${emp[5]}")
        print(f"Total Discount: ${emp[4]}")

        # Ask user to go back or exit
        while True:
            choice = input("Enter 1 to go back to menu or 2 to exit: ")
            if choice == "1":
                employee_discount_program()
            elif choice == "2":
                exit()
            else:
                print("Error: invalid choice.")


def get_employee_summary(employee_list):
    print("All-Employee Summary Page")
    emp_menu = ["Employee ID", "Employee Name", "Employee Type", "Years Worked", "Total Purchased", "Total Discounts"]
    print(f"{emp_menu[0]:<10} | {emp_menu[1]:<10} | {emp_menu[2]:<10} | {emp_menu[3]:<10} | {emp_menu[4]:<10} | {emp_menu[5]}")

    for emp in employee_list:
        print(f"{emp[0]:<12}| {emp[1]:<14}| {emp[2]:<14}| {emp[3]:<13}| ${emp[5]:<15}| ${emp[4]}")

    # Ask user to go back or exit
    while True:
        choice = input("Enter 1 to go back to menu or 2 to exit: ")
        if choice == "1":
            employee_discount_program()
        elif choice == "2":
            exit()
        else:
            print("Error: invalid choice.")


def employee_discount_program():
    print_menu()
    get_menu_option()


employee_discount_program()
