n=5
k=0
for i in range(n-1):
    for j in range(n):
        print(j+1+k,end="\t")
    k+=n
    print()