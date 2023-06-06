n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    if l.count(i)==i:
        if i not in p:
            p.append(i)
if len(p)==0:
    print("-1")
else:
    print(min(p),max(p))