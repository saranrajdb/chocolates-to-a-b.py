n=int(input())
for i in range(n,0,-1):
    for j in range(1,n+1):
        if i>j:
            if i+j==n:
                print(i,j)

if n%2==0:
    print(n//2-1)
else:
    print(n//2)