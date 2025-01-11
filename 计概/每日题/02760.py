#数字三角形 dp
def f(i,j):
    if i==n-1:
        dp[i][j]=numbers[i][j]
        return dp[i][j]
    if dp[i][j]!=0:
        return dp[i][j]
    else:
        dp[i][j]=numbers[i][j]+max(f(i+1,j),f(i+1,j+1))
        return dp[i][j]

n = int(input())
numbers=[]
for _ in range(n):
    numbers.append(list(map(int, input().split())))

dp=[[0]*n for _ in range(1,n+1)]

print(f(0,0))