matrix=[list(map(int,input().split())) for _ in range(5)]
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            position=[i+1,j+1]
            break

a,b=position
moves=abs(a-3)+abs(b-3)
print(moves)
