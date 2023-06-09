n,m=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
l=[]
for i in n:
    if i not in m:
        if i not in l:
            l.append(i)
for i in m:
    if i not in n:
        if i not in l:
            l.append(i)
print(len(l))