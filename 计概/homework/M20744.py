a=list(map(int,input().split(',')))
n=len(a)
dp1=[0]*n #以第i个元素结尾的最大子序列和，不放回
dp2=[0]*n #以第i个元素结尾的最大子序列和，且可以放回一个元素
dp1[0]=a[0]
dp2[0]=a[0]
for i in range(1,n):
    dp1[i]=max(dp1[i-1]+a[i],a[i])
    dp2[i]=max(dp1[i-1],dp2[i-1]+a[i],a[i]) #dp1[i-1]放回当前元素

print(max(dp2))