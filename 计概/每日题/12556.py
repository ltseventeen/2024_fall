s=input().lower()
answer=[]
pre=s[0]
count=1
for i in range(1,len(s)):
    if s[i]==pre:
        count+=1
    else:
        answer.append(f'({pre},{count})')
        pre=s[i]
        count=1
answer.append(f'({pre},{count})')
print(''.join(answer))