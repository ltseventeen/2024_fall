n,m,k=map(int,input().split())
maze=[]
for _ in range(n):
    maze.append(list(map(int,input().split())))

visited=[[False]*m for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

can_reach=False

def is_valid(x,y,step):
    return 0<=x<n and 0<=y<m and maze[x][y]==0 and step<=k and not visited[x][y]

def dfs(x,y,step):
    global can_reach

    if can_reach:
        return

    if x==n-1 and y==m-1 and step==k:
        can_reach=True
        return

    visited[x][y]=True

    for i in range(4):
        next_x=x+dx[i]
        next_y=y+dy[i]
        if is_valid(next_x,next_y,step+1):
            dfs(next_x,next_y,step+1)

    visited[x][y]=False

dfs(0,0,0)
if can_reach:
    print("Yes")
else:
    print("No")
