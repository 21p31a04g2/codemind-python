s=input().split()
s.sort()
s.sort(key=len)
print(*s)