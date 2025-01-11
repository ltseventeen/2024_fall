n=int(input())
sum_n=0
for i in range(1,n+1):
    if i%7==0 or (str(7) in str(i)):
        continue
    else:
        sum_n+=i**2
print(sum_n)