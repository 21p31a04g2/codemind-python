s=input()
s1=list(s.split())
for i in range(len(s1)):
    if i%2==0:
        s1[i]=s1[i][::-1]
    print(s1[i],end=' ')