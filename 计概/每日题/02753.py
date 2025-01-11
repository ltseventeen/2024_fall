#斐波那契数列
n=int(input())
dp=[-1]*21
dp[0]=0
dp[1]=1

def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        if dp[n]!=-1:
            return dp[n]
        else:
            dp[n]=f(n-1)+f(n-2)
            return dp[n]


for _ in range(n):
    a=int(input())
    print(f(a))