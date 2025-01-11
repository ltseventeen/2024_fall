n=int(input())
cnt=0
for _ in range(n):
    t,k=input().split()
    t=float(t)
    k=int(k)
    if t>=37.5 and k==1:
        cnt+=1
    else:
        continue

print(cnt)