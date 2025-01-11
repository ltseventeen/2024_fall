import math
determine_2with3=[0,5,3,1]

while True:
    n1,n2,n3,n4,n5,n6 = map(int,input().split())
    if n1+n2+n3+n4+n5+n6==0:
        break
    boxes = n4+n5+n6+math.ceil(n3/4)
    spaceleft_for_b = n4*5 + determine_2with3[n3%4]
    if n2 > spaceleft_for_b:
        boxes += math.ceil(n2-spaceleft_for_b/9)
    spaceleft_for_a = (boxes-n6)*36-n5*25-n4*16-n3*9-n2*4
    if n1 > spaceleft_for_a:
        boxes += math.ceil(n1-spaceleft_for_a/36)
    print(boxes)
