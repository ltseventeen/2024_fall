from collections import deque

#方向数组
dx=[0,0,1,-1]
dy=[1,-1,0,0]

n=int(input())
for _ in range(n):
    r,c,k=map(int,input().split())
    maze=[]
    for _ in range(r):
        maze.append(list(input()))

    #初始化起点和终点的坐标
    sx,sy,ex,ey=-1,-1,-1,-1
    for i in range(r):
        for j in range(c):
            if maze[i][j]=='S':
                sx,sy=i,j
            if maze[i][j]=='E':
                ex,ey=i,j

    #bfs
    queue=deque()
    queue.append((sx,sy,0))  #初始位置和时间
    times=[[[float('inf')]*k for _ in range(c)] for _ in range(r)]  #记录到达每个点的最短用时,按t%k分类
    times[sx][sy][0]=0

    found=False  #是否找到终点
    while queue:
        x,y,t=deque.popleft(queue)

        #检查是否到达出口
        if (x,y)==(ex,ey):
            print(t)
            found=True
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            nt=t+1
            nk=nt%k

            if 0<=nx<r and 0<=ny<c:
                # 如果下一步的时间是K的倍数，那么可以走任何位置；否则检查目标位置是否为石头
                if nk==0 or maze[nx][ny]!='#':
                    if nt<times[nx][ny][nk]:
                        times[nx][ny][nk]=nt
                        queue.append((nx,ny,nt))

    if not found:
        print('Oop!')