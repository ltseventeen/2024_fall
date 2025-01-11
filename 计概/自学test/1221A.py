q=int(input())

for _ in range(q):
    n=int(input())
    a=list(map(int,input().split()))

    if 2048 in a:
        print("YES")
    else:
        num=0
        for i in range(0,11):
            num1=a.count(2**i)+num #以1为例，统计a中1的个数，把他们全部合成2
            num=num1//2 #更新num的值为现在新增的2的个数
        if num>=1:
            print("YES")
        else:
            print("NO")