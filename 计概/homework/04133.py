d=int(input())
n=int(input())
matrix=[[0]*1025 for _ in range(1025)]

dx=[_ for _ in range(-d,d+1)]
dy=[_ for _ in range(-d,d+1)] #从-d到d是垃圾周围安放炸弹可以炸毁那一堆垃圾的范围

for _ in range(n):
    x,y,i=map(int,input().split())
    for m in dx:
        for n in dy:
            if 0<=x+m<1025 and 0<=y+n<1025: #判断是否超出边界
                matrix[x+m][y+n]+=i #把炸毁垃圾的数量加给对应的投放点

#输出清理垃圾最多的投放点数目和清理垃圾数目
max_num=0
max_waste=0
for i in range(1025):
    for j in range(1025):
        if matrix[i][j]>max_waste:
            max_waste=matrix[i][j]
            max_num=1
        elif matrix[i][j]==max_waste:
            max_num+=1

print(max_num,max_waste)