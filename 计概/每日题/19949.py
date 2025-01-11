n=int(input())
num=0
for _ in range(n):
    s=str(input()).replace('### ###',' ')
    num+=int(s.count('###')/2)
print(num)