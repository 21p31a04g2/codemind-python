n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
l=[]
sum=0
for i in range(n):
    for j in range(m):
        if i==j or i+j==n-1:
            sum+=mat[i][j]
print(sum)
            