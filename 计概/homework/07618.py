n=int(input())
old=[]
normal=[]

for _ in range(n):
    name,age=input().split()
    age=int(age)
    if age>=60:
        old.append((name,age))
    else:
        normal.append((name,age))

sort_old=sorted(old,key=lambda x:x[1],reverse=True)
l=sort_old+normal
name_list=[name for name,age in l]

print('\n'.join(name_list))
