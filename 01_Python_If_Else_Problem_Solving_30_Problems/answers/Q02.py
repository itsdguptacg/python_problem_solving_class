number=int(input("Enter the Number : ").strip())
if number>0:
    if number%2==0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
elif number<0:
    if number%2==0:
        print("Negative Even Number")
    else:
        print("Negative Odd Number")
elif number==0:
    print("Zero")
else:
    print("Invalid Input")