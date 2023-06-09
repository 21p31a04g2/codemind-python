n,m=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
l=[]
for i in n:
    if i in m:
        if i not in l:
            l.append(i)
print(*l)