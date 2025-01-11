#构建平方数列表
squares=[]
for i in range(1,10**5):
    if i**2<=10**9:
        squares.append(i**2)

#平方数判定
def is_square(n):
    return n in squares

def is_blessed_id(A):
    num=list(map(int,str(A)))

    def dfs(i):
        if i==len(num):
            return True

        n=0
        for j in range(i,len(num)):
            n=n*10+num[j]
            if is_square(n):
                if dfs(j+1):
                    return True
        return False

    return dfs(0)

A=int(input())
if is_blessed_id(A):
    print("Yes")
else:
    print("No")
