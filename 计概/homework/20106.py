from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

m,n,p=map(int,input().split())
landscape=[]
for _ in range(m):
    landscape.append(list(input().split()))

for _ in range(p):
    x1,y1,x2,y2=map(int,input().split())
    if landscape[x1][y1]=='#' or landscape[x2][y2]=='#':
        print('NO')
    else:
        queue=deque()
        force = [[float('inf')] * n for _ in range(m)]  # 记录到达每个点所需要的最小体力值
        force[x1][y1]=0
        queue.append((x1,y1))
        can_reach=False

        while queue:
            x,y=deque.popleft(queue)
            if x==x2 and y==y2:
                can_reach=True

            for i in range(4):
                nf=force[x][y]
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<m and 0<=ny<n and landscape[nx][ny]!='#':
                    nf+=abs(int(landscape[nx][ny])-int(landscape[x][y]))
                    if nf<force[nx][ny]:
                        force[nx][ny]=nf
                        queue.append((nx,ny))

        if not can_reach:
            print('NO')
        else:
            print(force[x2][y2])