# 作者: 余畅
# 2025年02月17日15时23分22秒
# fyzcxfyzcx@gmail.com

def use_cal():
    """
    算术运算符
    :return:
    """
    result = 5 // 2
    print(result)
    result1 = 5 % 2
    print(result1)
    print(10 ** 3)


def use_logic():
    """
    使用逻辑运算符
    :return:
    """
    print(3 and 5)  # 都真返回后1个
    print(1 or 2)  # 都真返回前1个
    # 短路运算
    a = 500
    a > 5 and print('a 大于5')
    b = 1
    b == 1 or print('这句话不会打印')


def use_bit():
    """
    熟练掌握位运算
    :return:
    """
    print(5 & 7)
    print(5 | 7)
    print(5 << 1)  # 左移是乘2
    print(10 >> 1)  # 右移除2，负数是减1除2
    print(-10 >> 1)
    print(9 >> 1)
    print(-9 >> 1)
    # 异或
    print('-' * 50)
    print(5 ^ 7 ^ 5)


# use_cal()
# use_logic()
use_bit()
