#定义整数转罗马数字的函数
def int_to_roman(n):
    #定义罗马数字的符号和值
    roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    #定义结果字符串
    result = ''

    #遍历罗马数字的符号和值
    for value,symbol in roman_dict.items():
        #从1000开始，计算当前值能整除的最大次数
        count = n//value
        #将当前符号重复count次添加到结果字符串中
        result += symbol*count

        #更新待转换的数字
        n -= value*count

    #返回
    return result

#定义罗马数字转整数的函数
def roman_to_int(n):
    #定义罗马数字的符号和值
    roman_dict_special = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
    roman_dict_usual = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    #定义结果整数
    result = 0

    #遍历罗马数字的符号和值,先特殊后普通
    for symbol,value in roman_dict_special.items():
        #如果当前符号在待转换的数字中出现，则将其转换为整数并加到结果中
        if symbol in n:
            count=n.count(symbol)
            result += value*count
            n=n.replace(symbol,'') #将当前符号从待转换的罗马数字中移除

    for symbol,value in roman_dict_usual.items():
        if symbol in n:
            count=n.count(symbol)
            result+=value*count
            n=n.replace(symbol,'')

    #返回结果
    return result

#读取输入
n = input()

#测试输入是否为整数
if n.isdigit():
    n=int(n)
    print(int_to_roman(n))
else:
    print(roman_to_int(n))