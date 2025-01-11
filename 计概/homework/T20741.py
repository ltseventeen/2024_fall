from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]
def find(x,y):
    a[x][y]=2
    q.append((0,(x,y))) #(step,(x,y))
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
            find(nx,ny)

def bfs(q,a):
    while q:
        step,(x,y)=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if a[nx][ny] == 1:
                    return step
                elif a[nx][ny]==0:
                    a[nx][ny]=2
                    q.append((step+1,(nx,ny)))



n=int(input())
a=[list(map(int,input())) for _ in range(n)]
q=deque()
ans=0

for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            find(i,j)
            ans=bfs(q,a)
            break
    if ans:
        break

print(ans)