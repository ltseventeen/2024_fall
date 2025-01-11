#读取输入
k=int(input()) #偏移量
s=list(input())

#定义函数
def puoyi(s,k):
    n=len(s)
    for i in range(n):
        #大写字母的破译
        if 'A' <=s[i]<='Z':
            m=ord(s[i])-k%26 #修正后的ASCII值
            if m<65: #如果修正后的ASCII值小于65，则需要加上26
                m+=26
            s[i]=chr(m)

        #小写字母的破译
        elif 'a' <=s[i]<='z':
            m=ord(s[i])-k%26
            if m<97:
                m+=26
            s[i]=chr(m)
    return ''.join(s)

#调用函数
print(puoyi(s,k))