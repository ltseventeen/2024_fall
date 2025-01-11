n=int(input())
act=[-1]*62

#数据预处理降低复杂度
for _ in range(n):
    start,end=map(int,input().split())
    start+=1
    end+=1
    if act[start]==-1:
        act[start]=end
    else:
        act[start]=min(act[start],end) #保留相同开始时间中结束时间最短的一项活动

dp=[0]*62
for i in range(1,62):
    if act[i]!=-1:
        for j in range(act[i]+1,62):
            dp[j]=max(dp[j],dp[i-1]+1)

print(max(dp))
