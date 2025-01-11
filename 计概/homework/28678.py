n=int(input())

while n>1:
     if n%2==0:
         print(str(n)+'/2='+str(int(n/2)))
         n=int(n/2)
     elif n%2==1:
         print(str(n)+'*3+1='+str(int(n*3+1)))
         n=int(n*3+1)

print('End')
