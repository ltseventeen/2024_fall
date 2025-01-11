import math
rest=[0,5,3,1]

while True:
    a,b,c,d,e,f = map(int,input().split())
    if a+b+c+d+e+f==0:
        break

    else:
        box=0
        box+=d+e+f #装4*4、5*5、6*6的箱子
        box+=math.ceil(c/4) #装3*3的箱子

        space_2=d*5+rest[c%4] #能和4*4、3*3一起装的2*2箱子
        if b>space_2:
            box+=math.ceil((b-space_2)/9) #装剩下的2*2箱子

        space_1=36*int(box)-36*f-25*e-16*d-9*c-4*b #剩余可以装1*1的空间
        if a>space_1:
            box+=math.ceil((a-space_1)/36)

        print(box)
