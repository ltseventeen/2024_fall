dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,m = map(int,input().split())
maze=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for i in range(n)]
min_steps=float('inf')

def is_valid(x,y):
    return 0<=x<n and 0<=y<m and not visited[x][y] and maze[x][y]!=1

def dfs(x,y,steps):
    global min_steps

    if x==n-1 and y==m-1:
        min_steps=min(min_steps,steps)
        return

    visited[x][y]=True

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if is_valid(nx,ny):
            dfs(nx,ny,steps+1)

    visited[x][y]=False

dfs(0,0,0)

if min_steps==float('inf'):
    print(-1)
else:
    print(min_steps)

#TLE