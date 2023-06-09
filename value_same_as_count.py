n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    if i not in p:
       if l.count(i)==i:
          p.append(i)
print(len(p))        