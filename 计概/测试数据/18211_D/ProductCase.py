import random
import sys
import os

# if len(sys.argv) != 2:
#     print("Usage: produceCase.py caseNum\n无输入程序将使用使用默认case数量20")
#     caseNum = 20
# else:
#     caseNum = int(sys.argc[1])

caseNum = 18

for i in range(caseNum):

    with open(str(i+1) + ".in", "w") as fout:
        m = random.randint(0, 5000)
        print(m, file=fout)

        num=random.randint(3, 50)
        for k in range(num):
            print(random.randint(0, 5000), file=fout, end=' ')


    os.system("python sampleCode.py < %d.in > %d.out" %(i+1, i+1))


caseNum = 2

for i in range(caseNum):

    with open(str(i + 19) + ".in", "w") as fout:
        m = random.randint(0, 5000)
        print(m, file=fout)

        num = 500
        for k in range(num):
            print(random.randint(0, 5000), file=fout, end=' ')

    os.system("python sampleCode.py < %d.in > %d.out" % (i + 19, i + 19))
