a,b=input().split()

#把ab中最后一个字母删掉，把剩下的数字转化为int型
a=int(a[:-1])
b=int(b[:-1])

print(a+b)