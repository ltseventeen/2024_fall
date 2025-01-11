n = int(input())
l=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2] #定义权重数组

for _ in range(n):
    s=input()
    x=sum(int(s[i])*l[i] for i in range(17)) #求和
    a=x%11 #求余数
    a_new=str((12-a)%11) #更新余数

    #处理10的特殊情况
    if a_new=='10':
        a_new='X'

    #比较是否一致
    if a_new==s[17]:
        print('YES')
    else:
        print('NO')

