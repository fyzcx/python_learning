# 作者: 余畅
# 2025年02月17日16时14分30秒
# fyzcxfyzcx@gmail.com

def use_while():
    # 1. 定义重复次数计数器
    i = 1

    # 2. 使用 while 判断条件
    while i <= 5:
        # 要重复执行的代码
        print("Hello Python")

        # 处理计数器 i
        i += 1

    print("循环结束后的 i = %d" % i)


def sum_100():
    i = 1
    result = 0
    # 2. 使用 while 判断条件
    while i <= 100:
        # 要重复执行的代码
        if i % 2 == 1:
            i += 1
            continue
        result += i
        # 处理计数器 i
        i += 1

    print(f'result={result}')


def sum_2000_break():
    i = 1
    result = 0
    # 2. 使用 while 判断条件
    while i <= 100:
        # 要重复执行的代码
        if result > 2000:
            break
        result += i
        # 处理计数器 i
        i += 1

    print(f'result={result},i={i}')


def use_for():
    """
    for的in后面必须是一个可迭代对象
    :return:
    """
    my_list = [5, 2, 3]  # my_list是一个列表，列表是可迭代类型的对象
    for i in my_list:
        print(i, end=' ')
    print()


def use_for_else():
    """
    for else中的else是for中没有从break，就一定会走else
    :return:
    """
    for i in range(10):
        if i == 15:
            print('i have 15')
            break
    else:
        print("don't find")
        print(i)  # 循环结束，如果没有break，i拿到的是最后一个元素


# use_while()
# sum_100()
# sum_2000_break()
# use_for()
use_for_else()
