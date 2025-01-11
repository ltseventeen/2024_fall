#小偷背包问题

n,b=map(int,input().split())
price=list(map(int,input().split()))
weight=list(map(int,input().split()))
dp=[[0]*(b+1) for _ in range(n+1)]

def value(n,b,price,weight,dp):
    for i in range(1,n+1):
        for j in range(1,b+1):
            if weight[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i-1]]+price[i-1])

    return dp[n][b]

print(value(n,b,price,weight,dp))