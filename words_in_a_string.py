s=input()
l=list(s.split())
p=[]
c=0
for i in l:
    if i not in p:
      c+=1
      p.append(c)
print(len(p))