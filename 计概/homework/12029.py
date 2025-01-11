from collections import deque
import sys

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    inq=set()
    inq.add((x,y))
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in inq and map_a[nx][ny]<map_a[sx][sy]:
                inq.add((nx,ny))
                q.append((nx,ny))
            if (i,j) in inq:
                return True

    return False

data = sys.stdin.read().split()
k = int(data[0])
index=1
for _ in range(k):
    m,n = map(int, data[index:index+2])
    index+=2
    map_a=[]
    for _ in range(m):
        map_a.append(list(map(int, data[index:index+n])))
        index+=n
    i,j=map(int, data[index:index+2])
    index+=2
    i-=1
    j-=1
    p=int(data[index])
    index+=1
    ans=0
    for _ in range(p):
        sx,sy=map(int, data[index:index+2])
        index+=2
        sx-=1
        sy-=1
        if map_a[sx][sy]<=map_a[i][j]:
            continue
        if ans>0:
            continue
        else:
            if bfs(sx,sy):
                ans+=1

    print("Yes" if ans>0 else "No")