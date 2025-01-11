k=int(input())
a=list(map(int,input().split()))
dp=[1]*(k)
for i in range(1,k):
    #dp[i]表示以i结尾的最多可以拦截的导弹的个数
    for j in range(i):
        if a[j]>=a[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))