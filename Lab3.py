# IS424
# Lab (3)

# { Ahmed Alahmed | 439 102 481 }

def emp_sal_program():
    print("Hello User, Welcome to the emp_sal_program..")
    try:
        programEngine = input("Please enter (s) to start the program or (e) to exit program: ")
        
        if programEngine.lower() == "s":
            empDic = {}
            checkValue = input("Enter [ (go) or any words to start adding] or (no) to stop: ")

            while checkValue.lower() != "no":
                empKey = input("Enter employee name: ")
                emp_keyValue = int(input("Enter employee salary: "))
                empDic[empKey] = emp_keyValue
                checkValue = input("Enter [ (a) or any words to continue adding] or (no) to stop: ")
            print("The dictionary of emp_salary_program is: ", empDic)
            print("Have a nice day user..")

        elif programEngine.lower() == "e":
            print("You have exited the program, have a nice day user..")
        else:
            print("User, try again with the same input..")
            emp_sal_program()
            
    except Exception as e:
        print("The problem is ",e," Or something went wrong, please try again..")
        emp_sal_program()

# Testing P1:
emp_sal_program()
