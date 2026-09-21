age=int(input("Enter Age : "))
if 18<=age<=120:
    print("Can Vote")
elif 0<=age<18:
    print("Cannot Vote")
else:
    print("Invalid Age")