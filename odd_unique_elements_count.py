n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if i not in a:
        a.append(i)
for i in a:
    if i not in b:
        if i%2!=0:
            b.append(i)
print(len(b))