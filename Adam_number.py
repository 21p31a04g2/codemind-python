n=int(input())
x=n*n
s=str(n)
y=int(s[::-1])#reverse of 12
z=y*y
s1=str(z)
m=int(s1[::-1])#reverse of 21 square
if x==m:#12 square is reverse to 21 square
    print(True)
else:
    print(False)
