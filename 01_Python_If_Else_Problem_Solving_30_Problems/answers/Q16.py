e_unit=int(input("Enter the number of units used : "))
if e_unit<=100 and e_unit>=0:
    print(f"Bill is {5*e_unit}")
elif e_unit<=200:
    print(f"Bill is {(5*100)+(7*(e_unit-100))}")
elif e_unit>200:
    print(f"Bill is {(5*100+7*100)+(10*(e_unit-200))}")
else:
    print("Invalid Input")