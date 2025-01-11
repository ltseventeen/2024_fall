
n,m=map(int,input().split())
maze=[]
for _ in range(n):
    maze.append(list(map(int,input().split())))

visited=[[False]*m for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

count = 0

def is_valid(x,y):
    return 0<=x<n and 0<=y<m and maze[x][y]==0 and not visited[x][y]

def dfs(x,y):
    global count

    if x==n-1 and y==m-1:
        count+=1
        return

    visited[x][y]=True

    for i in range(4):
        next_x=x+dx[i]
        next_y=y+dy[i]
        if is_valid(next_x,next_y):
            dfs(next_x,next_y)

    visited[x][y]=False

dfs(0,0)
print(count)
