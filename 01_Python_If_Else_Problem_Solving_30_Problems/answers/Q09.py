marks=int(input("Enter Marks : "))
print("Grade is",end=" ")
if 100>=marks>=90:
    print("A")
elif 89>=marks>=80:
    print("B")
elif 79>=marks>=70:
    print("C")
elif 69>=marks>=60:
    print("D")
elif 59>=marks>=40:
    print("E")
elif 40>marks>=0:
    print("Fail")
else:
    print("Invalid marks")