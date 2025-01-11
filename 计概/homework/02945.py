#拦截导弹

k=int(input())
a=list(map(int,input().split()))
dp=[1]*k

for i in range(k):
    for j in range(i):
        if a[j]>=a[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))