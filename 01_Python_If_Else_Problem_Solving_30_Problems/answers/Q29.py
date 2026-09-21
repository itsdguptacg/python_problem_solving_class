nu1=int(input("Enter The Number 1: "))
nu2=int(input("Enter The Number 2: "))
nu3=int(input("Enter The Number 3: "))
if nu1>nu2>nu3:
    print(nu2)
elif nu2>nu3>nu1:
    print(nu3)
elif nu3>nu1>nu2:
    print(nu1)