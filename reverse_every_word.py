s=input()
w=s.split()
x=[i[::-1] for i in w]
nw=" ".join(x)
print(nw)