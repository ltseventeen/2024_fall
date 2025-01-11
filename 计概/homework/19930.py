from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    global min_step

    q=deque()
    q.append((0,(x,y))) #(step,(x,y))
    inq=set()
    inq.add((x,y))

    while q:
        step,(x,y)=q.popleft()
        if graph[x][y]==1:
            min_step=min(min_step,step)
            return

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if graph[nx][ny]!=-1 and graph[nx][ny]!=2 and (nx,ny) not in inq:
                inq.add((nx,ny))
                q.append((step+1,(nx,ny)))

m,n = map(int,input().split())
graph=[[-1]*(n+2)]+[[-1]+list(map(int,input().split()))+[-1] for i in range(m)]+[[-1]*(n+2)]
min_step=float('inf')

bfs(1,1)
if min_step==float('inf'):
    print('NO')
else:
    print(min_step)