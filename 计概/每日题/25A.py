n=int(input())
lst=list(map(int,input().split()))

#定义函数evenness，找出奇偶性不同的数的索引
def evenness(lst):
    for i in range(n):
        lst[i]=lst[i]%2 #将列表中的数转化成0&1，0表示偶数，1表示奇数
    even_num=lst.count(0) #计算偶数的个数
    odd_num=lst.count(1) #计算奇数的个数
    #判断奇数多还是偶数多
    #也可以直接求和，是1的话就只有一个奇数返回这个奇数的索引，不是1的话返回0（偶数）的索引
    if even_num>odd_num:
        return lst.index(1)+1
    elif even_num<odd_num:
        return lst.index(0)+1

order=evenness(lst)

print(order)