num1=int(input("Enter the First Number : "))
num2=int(input("Enter the Second Number : "))
num3=int(input("Enter the Third Number : "))
if num1<num2 and num1<num3:
    print(f"{num1} is Smallest")
elif num2<num1 and num2<num3:
    print(f"{num2} is Smallest")
elif num3<num1 and num3<num2:
    print(f"{num3} is Smallest")
else:
    print("Not Values to Compare Please Enter different Numbers To compare")