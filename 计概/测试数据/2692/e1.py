n = int(input())

for _ in range(n):
    a = []
    coins = 'ABCDEFGHIJKL'

    for i in range(3):
        row = list(input().split())
        a.append(row)

    for i in coins:
        flag = 1
        light = False
        heavy = False

        for j in a:
            if i in j[0] or i in j[1]:
                if j[2] == "even":
                    flag = 0
                    break

        if flag == 1: 
            for j in a:
                if i in j[0]:
                    if j[2] == "up":
                        heavy = True
                    elif j[2] == "down":
                        light = True
                elif i in j[1]:
                    if j[2] == "up":
                        light = True
                    elif j[2] == "down":
                        heavy = True

            if light:
                print("{} is the counterfeit coin and it is light.".format(i))
            elif heavy:
                print("{} is the counterfeit coin and it is heavy.".format(i))
