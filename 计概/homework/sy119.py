#汉洛塔
def times(n):
    if n==1:
        return 1
    else:
        return 2*times(n-1)+1

def steps(n):
    if n==1:
        return "A->C"
    else:
        temp_char='X'
        step1=steps(n-1).replace('B',temp_char).replace('C','B').replace(temp_char,'C')

        step2='A->C'

        step3=steps(n-1).replace('B',temp_char).replace('A','B').replace(temp_char,'A')
        return step1+'\n'+step2+'\n'+step3

n=int(input())
print(times(n))
print(steps(n))