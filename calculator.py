print("----WELCOME to Calculator----")
def simple_calculator():
    a=float(input("Enter the First Number :"))
    b=float(input("Enter the Second Number :"))
    
    Operation = input("Please enter the Mathematical Operation you want to perform (such as +,-,*,/) :")
    
    def add():
        return (a+b)

    def substract():
        return(a-b)

    def product():
        return(a*b)

    def divide():
        return(a/b)

    if Operation =="+":
        print("The Addition of",a,"and",b,"is",add())
    elif Operation =="-":
        print("The Substraction of",a,"and",b,"is",substract())
    elif Operation =="*":
        print("The Multiplication of",a,"and",b,"is",product())
    elif Operation =="/":
        print("The Division of",a,"and",b,"is",divide())
    else:
        print("Invalid operation, please enter basic mathematical operator")
    
    ans = input("Do you want to calculate again?\n Please type YES or NO.\n")

    if ans== 'YES' or ans=='Yes' or ans=='yes':
        simple_calculator()

    elif ans== 'NO' or ans== 'No' or ans== 'no':
        print("See you later.")

    elif ans !="YES" or ans !="Yes" or ans !="yes" or ans !="NO" or ans !="no" or ans !="No" :
        print("Invalid Input!!") 
        ans = input(" Please type YES or NO only\n")
        simple_calculator()
    else:
        print("Invalid Input!")

simple_calculator()
