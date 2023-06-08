s=input().lower()
c=0
for i in s:
    if i!=' 'and s.count(i)==1:
        c+=1
print(c)