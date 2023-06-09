s=input()
l=list(s.split())
c=0
p=[]
for i in l:
    if i in l:
        p.append(l.count(i))
print(len(p))
        
        