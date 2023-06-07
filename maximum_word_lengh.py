s=input()
l=list(s.split())
p=[]
for i in l:
    if i not in p:
        p.append(len(i))
print(max(p))