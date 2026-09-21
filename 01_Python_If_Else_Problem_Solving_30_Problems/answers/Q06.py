num=int(input("Enter The Number : "))
if num%5==0 and num%11==0:
    print(f"{num} is Divisible by 5 and 11")
elif num%5==0:
    print(f"{num} is Divisible by 5")
elif num%11==0:
    print(f"{num} is Divisible by 11")
else:
    print(f"{num} is neither Divisible by 5 or 11")