n=int(input())
maze=[[0]*3]
for _ in range(n):
    maze.append([0]+list(map(int,input().split()))+[0])
#print(maze)

dp=[[0]*3]
for i in range(1,n+1):
    dp.append([0]*(i+2))
dp[1][1]=maze[1][1]
#print(dp)

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+maze[i][j]

#print(dp)
print(max(dp[n]))
