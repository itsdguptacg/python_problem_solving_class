l1=int(input("Enter the Length of side 1 : "))
l2=int(input("Enter the Length of side 2 : "))
l3=int(input("Enter the Length of side 3 : "))
if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print("Is a valid triangle")
else:
    print("is Not a valid Triangle")