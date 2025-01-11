n=int(input())
a0,b0=map(int,input().split())
total=a0
m=1
for _ in range(n):
    a,b=map(int,input().split())
    total*=a
    m=max(m,a*b)

print(total//m)