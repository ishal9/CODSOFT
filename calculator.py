def calculate():
    num1=int(input("Enter your first number: "))
    num2=int(input("Enter your second number: "))
    operation = input("Please enter the Mathematical Operation you want to perform (such as +,-,*,/)")

    if operation == '+':
        print("{} + {} = ".format(num1, num2))
        print(num1+ num2)

    elif operation == '-':
        print("{} - {} = ".format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        print("{} * {} = ".format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        print("{} / {} = ".format(num1, num2))
        print(num1 / num2)

    else:
        print("Invalid Operator, please enter basic mathematical operator \n")

    calculator_again = input("Do you want to calculate again?\n Please type YES or NO.\n")

    if calculator_again== 'YES' or calculator_again=='Yes' or calculator_again=='yes':
        calculate()

    elif calculator_again== 'NO' or calculator_again== 'No' or calculator_again== 'no':
        print("See you later.")

    else:
        
        again()

calculate()
