def selfnum(num):
    temp=num
    while temp:
        d=temp%10
        temp=temp//10
        if d==0 or num%d!=0:
            return False
    return True

n=int(input())
m=int(input())
for i in range(n,m+1):
    if selfnum(i):
        print(i,end=" ")