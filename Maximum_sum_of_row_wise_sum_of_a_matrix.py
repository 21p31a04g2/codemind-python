n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
l=[]
maxsum=0
for i in range(n):
    sum=0
    for j in range(m):
        sum+=mat[i][j]
    if sum>maxsum:
            maxsum=sum
            l.append(maxsum)
print(max(l))
            