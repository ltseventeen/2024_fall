name=input()
table=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=0
for i in table:
    if i in name:
        number+=1
    else:
        continue

if number%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")