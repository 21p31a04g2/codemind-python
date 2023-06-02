n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
p=[]
for i in l:
    if i in range(a,b+1):
        p.append(i)
if len(p)==0:
    print("-1")
else:
    print(max(p))