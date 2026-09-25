n=int(input("Enter the number: "))
k=0
for i in range(n):
    for j in range(n):
        print(j+1+k,end="\t")
    k+=n
    print()