n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
k=[]
for i in l:
    if i in range(a,b+1):
        k.append(i)
print(sum(k))
        