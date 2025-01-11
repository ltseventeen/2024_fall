#思路：如果一个数不是二的n次方，则其有奇数除数。因此，我们只需要判断这个数是否是2的n次方
t=int(input())
for i in range(t):
    n=int(input())
    while n%2==0:
        n//=2
    if n>=1:
        print('YES')
    else:
        print('NO')
