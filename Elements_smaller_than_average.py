n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    a=sum(l)//len(l)
    if l[i]<=a:
        c+=1
print(c)