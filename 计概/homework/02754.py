#八皇后
#i是从0开始数的，j是从1开始数的

def queen(x):
    result = []
    queen_list = [0]*x

    def place(i):
        if i==x:
            result.append(queen_list.copy())
        else:
            for j in range(1,9):
                if not is_attack(i,j):
                    queen_list[i]=j
                    place(i+1)
                    #如果发现下一行每一个位置都无法放皇后，会跳出place(i+1)函数，来到本行
                    queen_list[i]=0

    def is_attack(i, j):
        for k in range(i):
            if j==int(queen_list[k]) or abs(i-k)==abs(j-int(queen_list[k])):
                return True
        return False

    place(0)

    return result

def get_queen_string(b):
    result=queen(8)
    queen_string=''.join(str(j) for j in result[b-1] )
    return queen_string

n=int(input())
for _ in range(n):
    b=int(input())
    print(get_queen_string(b))