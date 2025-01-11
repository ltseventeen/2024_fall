# pylint: skip-file
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[-1,1,-2,2,-2,2,-1,1]

def dfs(x,y,dep):
    global count

    if dep==n*m:
        count+=1
        return

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and not visited[x][y]

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if is_valid(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny, dep+1)
            visited[nx][ny] = False


t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    count=0
    dep=1
    dfs(x,y,dep)
    print(count)