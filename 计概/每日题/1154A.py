#读取输入的四个数
x1,x2,x3,x4=map(int,input().split())
numbers=[x1,x2,x3,x4]

#找出其最大值即为a+b+c
sum_abc=max(x1,x2,x3,x4)
numbers.remove(sum_abc)#更新列表

#最大值分别减剩下的三个数就是abc
for i in numbers:
    print(sum_abc-i,end=' ')