s=input().lower()
l=[]
for i in s:
    if i!=' 'and s.count(i)==1:
        l.append(i)
if len(l)==0:
    print("-1")
else:
    print(l[0])