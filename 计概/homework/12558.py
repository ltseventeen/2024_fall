n,m=map(int,input().split()) #读取行数，列数
a=[[] for _ in range(n+2)] #搞n+2个空列表是为了方便加一圈保护圈

a[0].extend([0]*(m+2)) #加第一行的保护圈
a[-1].extend([0]*(m+2)) #加最后一行的保护圈
for i in range(1,n+1):
    a[i].extend([0]+list(map(int,input().split()))+[0]) #读取输入，顺便加上保护圈

l=0 #初始化周长
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]==1:
            l+=4-(a[i][j-1]+a[i][j+1]+a[i-1][j]+a[i+1][j]) #如果遇到岛屿，计算它周围有几个1，4减去其就是周围海水的数量，即周围的边长

print(l) #输出周长