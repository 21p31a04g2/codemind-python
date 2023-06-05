n=int(input())
l=list(map(int,input().split()))
s=n//2
s1=0
s2=0
for i in range(0,s):
    s1+=l[i]
for i in range(s,n):
    s2+=l[i]
print(abs(s1-s2))
    