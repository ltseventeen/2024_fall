n,m1,m2=map(int,input().split())
a=[[0]*n for _ in range(n)]
b=[[0]*n for _ in range(n)]

#修改矩阵a,b的值
for _ in range(m1):
    i,j,num=map(int,input().split()) #第i行，第j列，值为num
    a[i][j]=num #i，j均从0开始

for _ in range(m2):
    i,j,num=map(int,input().split())
    b[i][j]=num

#计算乘法
c=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        #C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + …… +A[i][n-1]*B[n-1][j]
        c[i][j]=sum(a[i][k]*b[k][j] for k in range(n))

#将c整理为三元组形式
result=[]
for i in range(n):
    for j in range(n):
        if c[i][j]!=0:
            result.append(f'{i} {j} {c[i][j]}')

#输出结果
print('\n'.join(result))