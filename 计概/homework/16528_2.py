n=int(input())
act=[[-1] for _ in range(62)]
for _ in range(n):
    s,e=map(int,input().split())
    act[e+1].append(s+1)

dp=[0]*62
for i in range(1,62):
    if max(act[i])==-1:
        for j in range(i):
            dp[i]=max(dp[i],dp[j])
    else:
        a=max(act[i])
        dp[i]=max(dp[i-1],dp[a-1]+1)

print(max(dp))