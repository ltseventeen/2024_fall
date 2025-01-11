from ast import literal_eval

def luoxuan(matrix,m,n):
    result=[]
    #给矩阵加保护圈，使得行和列都从1开始
    matrix.insert(0,[0]*(n+2))
    matrix.append([0]*(n+2))
    for i in range(1,m+1):
        matrix[i].insert(0,0)
        matrix[i].append(0)

    #从左上角开始遍历
    i=1
    j=1
    result.append(matrix[1][1])
    while True:
        j+=1
        while i+j<=n+1:
            #从左往右
            result.append(matrix[i][j])
            j+=1
            if i+j>n+1:
                j-=1
                break
        #边界判断
        if i+j==n+1 and i-j==m-n:
            break

        i+=1
        while i-j<=m-n:
            #从上往下
            result.append(matrix[i][j])
            i+=1
            if i-j>m-n:
                i-=1
                break
        #边界判断
        if i-j==m-n and i+j==m+1:
            break

        j-=1
        while j+i>=m+1:
            #从右往左
            result.append(matrix[i][j])
            j-=1
            if j+i<m+1:
                j+=1
                break
        #边界判断
        if j+i==m+1 and i-j==1:
            break

        i-=1
        while i-j>=1:
            #从下往上
            result.append(matrix[i][j])
            i-=1
            if i-j<1:
                i+=1
                break
        #边界判断
        if i-j==1 and j+i==n+1:
            break

    return result




matrix=literal_eval(input())
m=len(matrix)
n=len(matrix[0])

result=luoxuan(matrix,m,n)
print(result)

