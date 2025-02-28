# 作者: 余畅
# 2025年02月18日10时32分42秒
# fyzcxfyzcx@gmail.com


def change(num):
    """
    整型是不可变类型，通过传参，函数内无法改变函数外某个整型变量的值
    :param num:
    :return:
    """
    print(f'num={num},id(num)={id(num)}')
    num = 5
    print(f'change函数内修改后 num={num},id(num)={id(num)}')


a = 10
print(f'id(a)={id(a)}')
change(a)
print(f'函数外a={a}')
print('-' * 50)
print('理解可变类型')
my_list = [1, 2, 3]
print(f'id(my_list)={id(my_list)}')


# my_list[0]=5
# print(f'id(my_list)={id(my_list)},my_list={my_list}')

def list_change(new_list):
    new_list[0] = 5  #  函数内修改列表的值
    print(f'list_change函数内{new_list},id(new_list)={id(new_list)}')


list_change(my_list)
print(f'list_change函数外 id(my_list)={id(my_list)},my_list={my_list}')
