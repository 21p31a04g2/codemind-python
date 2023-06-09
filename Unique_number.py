n=list(input())
p=[]
for i in n:
    if i in n:
        if i not in p:
            p.append(i)
if len(n)==len(p):
    print("Unique Number")
else:
    print("Not Unique Number")