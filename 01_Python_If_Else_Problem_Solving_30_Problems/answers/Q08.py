marks=int(input("Enter Marks : "))
if marks>=40 and marks<=100:
    print("Pass")
elif marks>=0 and marks<40:
    print("Fail")
else:
    print("Invalid Marks")