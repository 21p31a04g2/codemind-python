n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    c=0
    if i<0:
        i=-i
    while i:
        c+=1
        i//=10
    p.append(c)
print(p.count(min(p)))