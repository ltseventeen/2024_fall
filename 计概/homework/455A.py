n=int(input())
l=list(map(int,input().split()))
s=[0]*100001

#统计出现次数
for i in l:
    s[i]+=1

#得分动态规划
dp=[[0,0] for _ in range(100001)]
for i in range(1,100001):
    #dp[i][0]表示值为i的元素不选，dp[i][1]表示值为i的元素选
    dp[i][0]=max(dp[i-1][0],dp[i-1][1])
    dp[i][1]=dp[i-1][0]+s[i]*i

print(max(dp[100000][0],dp[100000][1]))