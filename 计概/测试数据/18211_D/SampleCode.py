P=int(input())
tokens = list(map(int, input().split()))

def solution1(tokens,P):
    tokens = sorted(tokens)
    score = 0
    maxscore = 0
    while (1):
        score_old = score
        poplist = []
        for x in range(len(tokens)):
            if (tokens[x] <= P):
                P -= tokens[x]
                score += 1
                poplist.append(x)

        for x in range(len(poplist)):
            tokens.pop(poplist[-(x + 1)])
        maxscore = max(maxscore, score)
        if (score > 0):
            for x in range(len(tokens)):
                P += tokens[-(x + 1)]
                score -= 1
                tokens.pop(-(x + 1))
                poplist.append(-1)
                break
        if (len(poplist) == 0):
            break
    return maxscore

print(solution1(tokens,P))