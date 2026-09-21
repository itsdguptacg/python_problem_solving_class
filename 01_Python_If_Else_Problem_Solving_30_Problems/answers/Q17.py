Choice = int(input("Choose From Following Operations\n1 > Addition\n2 > Subtraction\n3 > Multiplication\n4 > Division\nYour Choice : "))
if Choice==1 or Choice==2 or Choice==3 or Choice==4:
    number1=int(input("Enter Number 1 : "))
    number2=int(input("Enter Number 2 : "))
    if Choice==1:
        print(f"Addition of {number1} and {number2} is {number1+number2}")
    elif Choice==2:
        print(f"Subtraction of {number1} and {number2} is {number1-number2}")
    elif Choice==3:
        print(f"Multiplication of {number1} and {number2} is {number1*number2}")
    elif Choice==4:
        if number2==0:
            print(f"Division of {number1} and {number2} is Not Valid")
        else:
            print(f"Division of {number1} and {number2} is {number1/number2}")
else:
    print("Invalid Choice")