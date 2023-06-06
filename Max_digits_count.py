n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    c=0
    if i<0:
        i=-i
    if i==0:
        i=1
    while i:
        c+=1
        i//=10
    p.append(c)
m=max(p)
print(p.count(m))