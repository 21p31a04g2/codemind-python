n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    if l[i]%2==0 and i%2!=0:
        s+=1
if s==0:
        print(True)
else:
    print(False)
        