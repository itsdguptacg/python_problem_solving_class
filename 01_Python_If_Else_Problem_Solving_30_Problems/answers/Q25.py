m1=float(input("Enter marks of Subject 1 : "))
m2=float(input("Enter marks of Subject 2 : "))
m3=float(input("Enter marks of Subject 3 : "))
if 0<=m1<=100 and 0<=m2<=100 and 0<=m3<=100:
    if 75<=m1<=100:
        print("Disitinction In Subject 1")
    if 75<=m2<=100:
        print("Disitinction In Subject 2")
    if 75<=m3<=100:
        print("Disitinction In Subject 3")
    if 60<=m1<=74:
        print("First Class In Subject 1")
    if 60<=m2<=74:
        print("First Class In Subject 2")
    if 60<=m3<=74:
        print("First Class In Subject 3")
    if 50<=m1<=59:
        print("Second Class In Subject 1")
    if 50<=m2<=59:
        print("Second Class In Subject 2")
    if 50<=m3<=59:
        print("Second Class In Subject 3")
    if 35<=m1<=49:
        print("Pass In Subject 1")
    if 35<=m2<=49:
        print("Pass In Subject 2")
    if 35<=m3<=49:
        print("Pass In Subject 3")
    if 0<=m1<35:
        print("Fail In Subject 1")
    if 0<=m2<35:
        print("Fail In Subject 2")
    if 0<=m3<35:
        print("Fail In Subject 3")
else:
    print("Invalid Input")