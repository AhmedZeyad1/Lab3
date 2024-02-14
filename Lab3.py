# IS424
# Lab (3)
# { Ahmed Alahmed | 439 102 481 }

# Q1 - Code:

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

# Testing Q1:
emp_sal_program()


print("\n")
print("==============================")
print("\n")


# Q2 - Code:

def largestValue():
    listOfValues = []

    for i in range(10):
        scanValue = float(input("User, enter index {}. value to add it to the list: ".format(i)))
        listOfValues.append(scanValue)
    print("The list is: ", listOfValues)

    theMaxValue = listOfValues[0]
    for x in listOfValues:
        if x > theMaxValue:
            theMaxValue = x
    print("The largest value in the list is: ", theMaxValue)

# Testing Q2:
largestValue()


print("\n")
print("==============================")
print("\n")


# Q3 - Code:
def convertTempCToF():
    try:
        tempInC = float(input("Enter the tempreture in (C): "))
        CtoF = ((9/5)*tempInC) + 32
        print("The tempreture before in C: ",tempInC," Now in F is ",CtoF)
    except Exception as e:
        print("The error is ",e," or something went wrong please try again..")
        convertTempCToF()

# Testing Q3:
convertTempCToF()                