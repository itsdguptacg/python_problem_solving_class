p1=input("Enter The name Like Examples\nPerson 1: Rahul 25\n\nPerson 1:").strip().split()
p2=input("\nPerson 2:").strip().split()
p3=input("\nPerson 3:").strip().split()
if int(p1[1])<int(p2[1]) and int(p1[1])<int(p3[1]):
    print(f"{p1[0]} is the Youngest")
elif int(p2[1])<int(p1[1]) and int(p2[1])<int(p3[1]):
    print(f"{p2[0]} is the Youngest")
elif int(p3[1])<int(p2[1]) and int(p3[1])<int(p1[1]):
    print(f"\n{p3[0]} is the Youngest\n\n")