n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    if i not in p:
        p.append(i)
if i in p:
    print(*p)