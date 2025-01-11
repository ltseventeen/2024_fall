def is_valid(x,y):
    return 0<=x<n and 0<=y<m and maze[x][y]==0 and not visited[x][y]

def dfs(x,y,now_value):
    global max_value

    if x==n-1 and y==m-1:
        if now_value>max_value:
            max_value=now_value
        return

    visited[x][y]=True

    for i in range(4):
        next_x=x+dx[i]
        next_y=y+dy[i]
        if is_valid(next_x,next_y):
            next_value=now_value+value[next_x][next_y]
            dfs(next_x,next_y,next_value)

    visited[x][y]=False

n,m=map(int,input().split())
maze=[]
value=[]
for _ in range(n):
    maze.append(list(map(int,input().split())))
for _ in range(n):
    value.append(list(map(int,input().split())))

visited=[[False]*m for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

max_value=float('-inf') #矩阵里的数可能是负的！！
now_value=value[0][0]

dfs(0,0,now_value)
print(max_value)
