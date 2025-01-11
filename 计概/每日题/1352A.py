t=int(input())
for _ in range(t):
    n=str(input())
    numbers=list(n)
    k=0
    round_numbers=[]
    for i in range(len(numbers)):
        if int(numbers[i])!=0:
            k+=1
            round_numbers.append(int(numbers[i])*(10**(len(numbers)-i-1)))
        else:
            continue
    output=' '.join(str(i) for i in round_numbers)
    print(k)
    print(output)

