# 作者: 余畅
# 2025年02月17日14时13分48秒
# fyzcxfyzcx@gmail.com

def use_float():
    """
    感受浮点数精度,准确是到16位
    :return:
    """
    f = 1234567891.2345678
    print(f)


def use_bool():
    """
    查看bool类型输出及运算
    :return:
    """
    print(1 == 1)
    print(True + 0)


def use_complex():
    """
    使用复数
    :return:
    """
    c = complex(3, 4)
    print("c is %d+%dj" % (c.real, c.imag))


def use_char():
    """
    转义字符
    :return:
    """
    print('abc\\edf')
    print("abc'd'efg'h")
    s = '''今天是一个好天气，'和"都在这里'''
    print(s)
    print('abc\rd')


def use_ascii():
    """
    使用 ASCII
    :return:
    """
    c = 'e'
    print(ord(c))  # 得到字符'a'的ASCII值
    d = chr(ord(c) - 32)
    print(d)


# use_float()
# use_bool()
# use_complex()
use_char()
# use_ascii()
