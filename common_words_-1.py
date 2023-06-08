s1=input().lower()
s2=input().lower()
l1=list(s1.split())
l2=list(s2.split())
c=0
for i in l1:
    if i in l2:
        c+=1
print(c)
        