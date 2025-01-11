stri=input().strip()
swap_stri=""
for char in stri:
    if char.isupper():
        swap_stri+=char.lower()
    elif char.islower():
        swap_stri+=char.upper()
    else:
        swap_stri+=char
#for循环的内容可以全部用swap_stri=stri.swapcase()代替，swapcase为自带的大小写转化函数
print(swap_stri)