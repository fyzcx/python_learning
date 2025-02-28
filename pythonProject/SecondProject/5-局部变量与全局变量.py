# 作者: 余畅
# 2025年02月18日10时59分09秒
# fyzcxfyzcx@gmail.com


def demo1():
    global num  # 如果要在函数内修改全局变量，必须global借用过来
    # print(num)
    num = 50
    print(num)


num = 100  # num是一个全局变量
demo1()
print(f'函数外num={num}')
