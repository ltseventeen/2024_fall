dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dp1(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]

    max_step=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c and h[nx][ny]<h[x][y]:
            max_step=max(max_step,dp1(nx,ny)+1)

    dp[x][y]=max_step
    return dp[x][y]

r,c=map(int,input().split())
h=[]
for _ in range(r):
    h.append(list(map(int,input().split())))
max_steps=1
dp=[[-1]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        max_steps=max(max_steps,dp1(i,j))

print(max_steps)