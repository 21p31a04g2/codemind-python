s=input()
l=list(s.split())
p=[]
for i in l:
    s=min(i)
    g=max(i)
    d=abs(ord(s)-ord(g))
    p.append(d)
print(*p)