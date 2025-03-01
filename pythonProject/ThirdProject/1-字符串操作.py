def use_str_base():
    str1 = "Hello,Python"
    for c in str1:
        print(c, end='')

    print()
    print(str1.find('ll'))  # 查找
    print(str1.replace('l', 'L', 1))  # 替换

    str_list = str1.split(',')
    print(str_list)
    print(type(str_list))

    print('-' * 50)
    str2 = 'hello\nworld\nhow are you\ntoday is a good day'
    str_list = str2.splitlines()
    print(str_list)

    str_result = ','.join(str_list)
    print(str_result)


def str_reverse():
    str1 = 'hello'
    my_list = list(str1)
    my_list.reverse()
    print(''.join(my_list))


str_reverse()
