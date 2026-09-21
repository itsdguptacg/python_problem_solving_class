year=int(input("enter The year : "))
if (year%400 == 0 and year>=0) or ((year%4==0 and year%100!=0) and year>=0):
    print(f"The {year} is Leap Year")
elif year<0:
    print("Enter a valid Year")
else:
    print(f"The {year} is not Leap Year")