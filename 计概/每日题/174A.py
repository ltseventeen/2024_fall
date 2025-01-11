t=int(input())

for _ in range(t):
    a=list(map(int,input().split()))
    a.sort()
    if a[2]==a[0]+a[1]:
        print("YES")
    else:
        print("NO")