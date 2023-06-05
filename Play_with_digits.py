n=int(input())
l=list(map(int,input().split()))
g=0
for i in l:
    while i:
        d=i%10
        g+=d
        i//=10
print(g)
