n,a,b,c=map(int,input().split())
l=[a,b,c]
dp=[0]+[float('-inf')]*n

for i in range(1,n+1):
    for j in range(3):
        if i>=l[j]:
            dp[i]=max(dp[i-l[j]]+1,dp[i])

print(dp[-1])