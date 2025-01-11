#优化空间复杂度的小偷背包

n,b=map(int,input().split())
price=list(map(int,input().split()))
weight=list(map(int,input().split()))
dp=[0]*(b+1)

for i in range(n):
    for j in range(b,weight[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weight[i]]+price[i])

print(dp[b])