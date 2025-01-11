m=int(input())
n=int(input())
l=list(map(str,input().split()))

#将数字按照两个数连起来最大的方式排序
for i in range(n):
    for j in range(i+1,n):
        if int(l[i]+l[j])<int(l[j]+l[i]):
            l[i],l[j]=l[j],l[i]

dp=[0]*(m+1)  #表示长度为i的最大整数
for num in l:
    for i in range(m,len(num)-1,-1):  #反向更新避免重复（？？）
        dp[i]=max(dp[i],int(str(dp[i-len(num)])+num))

print(dp[m])