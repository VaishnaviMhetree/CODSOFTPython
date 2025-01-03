def calculator():
    print("_______CALCULATION_______")
    num_1=float(input("Enter first number:"))
    num_2=float(input("Enter second number:"))
    while True:
        operation=int(input("Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\nEnter 5 to Exit"))
        if operation==1:
            print("_______ADDITION_______")
            print(num_1+num_2)
        elif operation==2:
            print("_______SUBTRACTION_______")
            print(num_1-num_2)
        elif operation==3:
            print("_______MULTIPICATION_______")
            print(num_1*num_2)
        elif operation==4:
            print("_______MULTIPICATION_______")
            print(num_1/num_2)
        elif operation==5:
            print("_______EXIT_______")
            break
        else:
            print("Invalid Input")
            break
calculator()

