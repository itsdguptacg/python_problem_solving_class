num=int(input("Enter The Number : "))
if num<0:
    print("Negative")
elif 0<=num<=10:
    print("Number is in Between 0 and 10")
elif 11<=num<=50:
    print("Number is in Between 11 and 50")
elif 51<=num<=100:
    print("Number is in Between 51 and 100")
else:
    print("Number is Above 100")
