n=int(input())
colors=list(input())
min_remove_count=0
for i in range(1,n):
    if colors[i]==colors[i-1]:
        min_remove_count+=1
    else:
        continue
print(min_remove_count)