s=input()
l=list(s.split())
s1=[]
s2=[]
for i in l:
    m1=ord(min(i))
    s1.append(m1)
    m2=ord(max(i))
    s2.append(m2)
    x=(sum(s1)-sum(s2))
print(abs(x))
    