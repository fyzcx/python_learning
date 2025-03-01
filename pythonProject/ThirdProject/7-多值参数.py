# 多值参数  函数的参数个数不确定


def demo1(num, num1, *args, **kwargs):
    print(num)
    print(num1)
    print(args)  # args吃掉所有的位置参数
    print(kwargs)  # kwargs吃掉所有的keyword参数


def demo(num, *args, **kwargs):
    demo1(num, *args, **kwargs)


demo(1, 2, name='小明', age=18, gender=True)
