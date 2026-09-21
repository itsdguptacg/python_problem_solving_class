hr=int(input("enter hour : "))
minute=int(input("enter minute : "))
seconds=int(input("enter seconds : "))
if 0<=hr<=23:
    if 0<=minute<=59:
        if 0<=seconds<=59:
            print("Valdi Time")
        else:
            print("Invalid Time")
    else:
        print("Invalid Time")
else:
    print("Invalid Time")