s=input().lower()
l=list(s.split())
p=[]
c=0
for i in l:
    if i==i[::-1]:
        c+=1
        p.append(c)
print(max(p))
    