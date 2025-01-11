a=input()

#将字符串转化为列表，以便修改。其中的单个字母是字符串格式
lst=list(a)
lst[0]=lst[0].upper()

#整理输出
print("".join(lst))