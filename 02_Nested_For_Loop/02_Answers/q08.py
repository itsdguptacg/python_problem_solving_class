n=int(input("Enter the number: "))
for i in range(n):
    for j in range(5):
        print((i+1)*(j+1),end=" ")
    print()

print("------- or alternate way -------")

n=int(input("Enter the number: "))
k=1
for i in range(n):
    for j in range(n):
        print((i+1)*k,end=" ")
    k+=1
    print()