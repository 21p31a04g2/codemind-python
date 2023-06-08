n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    if l[i] in l:
        s+=l[i]
print(s)