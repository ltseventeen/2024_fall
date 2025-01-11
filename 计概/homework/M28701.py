n,k=map(int,input().split())
t=list(map(int,input().split()))
t.sort(reverse=True)
s=sum(t)
for i in range(n):
    if t[i]>s/k:
        s-=t[i]
        k-=1

print(f'{s/k:.3f}')