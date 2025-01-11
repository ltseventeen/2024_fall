t,k=map(int,input().split())
mod=10**9+7
dp=[0]*(10**5+1)
s=[0]*(10**5+1)
dp[0]=1
s[0]=0
for i in range(1,10**5+1):
    if i<k:
        dp[i]=dp[i-1]%mod
    else:
        dp[i]=(dp[i-1]+dp[i-k])%mod
    s[i]=(s[i-1]+dp[i])%mod

for _ in range(t):
    a,b=map(int,input().split())
    answer=(s[b]-s[a-1])%mod
    print(answer)