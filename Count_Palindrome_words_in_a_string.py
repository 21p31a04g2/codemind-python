s=input().lower()
l=list(s.split())
c=0
for i in l:
    if i[::-1]==i:
      c+=1
print(c)
