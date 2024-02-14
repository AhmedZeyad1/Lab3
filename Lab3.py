# IS424
# Lab (3)
# { Ahmed Alahmed | 439 102 481 }


# 1st. Program:
def emp_sal_program():
    try:
        print("Hello User,, Welcome to the emp_sal_program..")
        
        checkValue = input("Please entre any words to start the program or (no) to stop.")

        while checkValue is not ("no" or "No" or "NO"):
            empKey = input("Enter employee name: ")
            empDic = {} == empKey

            emp_keyValue = input(int)("Enter employee salary: ")
            empDic[empKey] == emp_keyValue
        print("The dictionory of emp_salary_program is: "+empDic)
        print("Have a nice day user")    
    except Exception (e):
        print("The problem is "+ e +" Or something went wrong, please try again..")
        emp_sal_scanner()


# Testing P1:
emp_sal_program()        