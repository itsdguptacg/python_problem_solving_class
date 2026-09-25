n=int(input("Enter the number: "))
for i in range(1,n*2,2):
    for j in range(1,i+1,2):
        print(j+1,end=" ")
    print()