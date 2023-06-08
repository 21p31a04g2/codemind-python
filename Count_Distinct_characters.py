s=input().lower()
l=[]
for i in s:
    if i!=' ' and i not in l:
        l.append(i)
print(len(l))
        
        