
#!/user/bin/even python
# -*- coding:utf-8 -*-


'''
字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。
例如：
输入：19
输出：2
输入：258
输出：2
输入：0219
输出：3
'''

def how_many_ways(digitarray):
    # implement here
    digitarray=str(digitarray)
    dp_list = [0] * (len(digitarray) + 1)
    dp_list[0] = 1
    for i in range(1, len(dp_list)):
        if digitarray[i - 1] != '0':
            dp_list[i] = dp_list[i - 1]*2
        if i != 1 and '09' < digitarray[i - 2:i] < '27':
            dp_list[i] += dp_list[i - 2]*2
        print(dp_list)
    print(dp_list[-1])
# how_many_ways(219)   # 结果16




# def how_many_ways(digitarray):
#     #如果数字是以“0”开头，将“0”去掉
#     digitarray = digitarray.lstrip('0')
#     length = len(digitarray)
#     #当去掉“0”后，数字的长度等于0时，直接返回0，因为0在条件里无法转换为字母
#     if length == 0:
#         return 0
#     #按照该数字的长度生成一个列表，用于后面进行计算
#     li = list(range(length+1))
#     li[0] = 1
#     print(li)
#     #循环去判断该数字的每一个值
#     for i in range(length+1):
#         #第一个数字不是0，肯定可以变换成一个字母
#         if i == 0:
#             continue
#         #前面一个字符如果不是'0'则li[i]至少等于li[i-1]
#         if digitarray[i-1] == '0':
#             li[i] = 1
#         else:
#             li[i] = li[i-1]      #判断当前字符跟前一个字符是否可以凑成一个字母所对应的值
#         if (i>1 and int(digitarray[i-1])<=6 and int(digitarray[i-2])==2) or (i>1 and int(digitarray[i-2])==1):
#             li[i] += li[i-2]
#     print(li)
#     return li[length]







for a in ["19","219","258"]:
    how_many_ways(a)



# num=how_many_ways('258')
# print(num)