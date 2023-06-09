s=input().lower()
l=list(s.split())
c=0
for i in l:
    if (i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u") and (i[-1]!="a" and i[-1]!="i" and i[-1]!="0" and i[-1]!="u" and i[-1]!="e"):
        c+=1
print(c)
        