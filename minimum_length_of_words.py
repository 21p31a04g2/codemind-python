s=input()
l=list(s.split())
p=[]
for i in l:
    if i in l:
        i=len(i)
        p.append(i)
print(min(p))
    