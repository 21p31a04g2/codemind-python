s1=input().lower()
s2=input().lower()
s3=set(s1)
s4=set(s2)
l=list(s3&s4)
c=0
for i in l:
    if i!='' and i.isalpha():
        c+=1
print(c)