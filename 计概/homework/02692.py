

n=int(input())
coins='ABCDEFGHIJKL'

def check(lines,coins):
    for line in lines:
        left,right,result=line
        left_weight=sum(weight[i] for i in left)
        right_weight=sum(weight[i] for i in right)

        if left_weight<right_weight and result!='down':
            return False
        if left_weight>right_weight and result!='up':
            return False
        if left_weight==right_weight and result!='even':
            return False
    return True

for _ in range(n):
    lines=[list(input().split()) for _ in range(3)]

    for i in coins:
        weight = {coin: 0 for coin in coins}
        found = False
        for w in [-1, 1]:
            weight[i] = w
            if check(lines,coins):
                found=True
                if w==-1:
                    print(f'{i} is the counterfeit coin and it is light.')
                elif w==1:
                    print(f'{i} is the counterfeit coin and it is heavy.')
                break

        if found:
            break
