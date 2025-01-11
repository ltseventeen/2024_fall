import re

def H_to_T(day,month,year):
    haab_month_list=['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu','uayet']
    t_month_list=['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
    #计算一共多少天
    days=year*365+haab_month_list.index(month)*20+day

    #计算T的日期
    t_year=days//260
    rest=days%260
    t_num=rest%13+1 #计算第一个数字
    t_month_index=rest%20 #计算月份的索引
    t_month=t_month_list[t_month_index] #获取月份的名称
    return f'{t_num} {t_month} {t_year}'


n=int(input())
print(n)

for _ in range(n):
    text=input()
    pattern=r'\.'
    replacement=' '
    text_new=re.sub(pattern,replacement,text)

    test_list=list(text_new.split()) #处理Haab年份文本

    day=int(test_list[0])
    month=test_list[1]
    year=int(test_list[2]) #获取打，month，year的信息

    output=H_to_T(day,month,year)
    print(output)