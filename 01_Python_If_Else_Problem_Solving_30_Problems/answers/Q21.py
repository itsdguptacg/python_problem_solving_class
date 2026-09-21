l1=int(input("Enter the Length of side 1 : "))
l2=int(input("Enter the Length of side 2 : "))
l3=int(input("Enter the Length of side 3 : "))
if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    if l1==l2 and l1==l3 and l2==l3:
        print("It is Equilateral triangle")
    elif l1==l2 or l1==l3 or l2==l3:
        print("It is Isosceles triangle")
    else:
        print("It is Scalene Triangle")
else:
    print("is Not a valid Triangle")