r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
s=0
l=[]
for i in range(r):
    for j in range(c):
        if i!=0 and j!=0 and i!=r-1 and j!=c-1:
            s+=mat[i][j]
l.append(s)
print(*l)