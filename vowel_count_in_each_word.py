def fun(n):
    c=0
    for i in n:
        if i in "aeiouAEIOU":
            c+=1
    return c
n=input().split()
l=[]
for i in n:
    l.append(fun(i))
print(*l)
        
        