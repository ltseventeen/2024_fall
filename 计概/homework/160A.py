n=int(input())
s=list(map(int,input().split()))
s.sort(reverse=True)
a=sum(s)

b=0 #初始化我的钱的总和
num=0 #初始化我拿到的硬币的数量
for i in range(n):
        if b>(a//2):
            break
        b+=s[i]
        num+=1

print(num)