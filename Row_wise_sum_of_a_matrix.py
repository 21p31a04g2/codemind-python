r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
l=[]
for i in range(r):
    s=0
    for j in range(c):
        s+=mat[i][j]
        if s not in l:
         l.append(s)
    print(s,end=" ")
        
        