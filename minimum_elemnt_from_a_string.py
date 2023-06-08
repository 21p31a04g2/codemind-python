n=input()
l=list(n.split())
s=l[-1]
m=min(s)
if m in s and m.lower() in s:
        print(m.lower())
else:
        print(m)
    