s=input()
c=0
l=[]
for i in "aeiou":
    if i not in s:
        l.append(i)
if len(l)==0:
    print("0")
else:
    for i in l:
        print(i,end=" ")