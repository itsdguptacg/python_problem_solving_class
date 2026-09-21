num=int(input("Enter The Number : "))
if num%3==0 and num%7==0:
    print(f"{num} is Divisible by 3 and 7")
elif num%3==0:
    print(f"{num} is Divisible by 3")
elif num%7==0:
    print(f"{num} is Divisible by 7")
else:
    print(f"{num} is neither Divisible by 3 or 7")