def demo1():
    num = int(input('请输入一个整数'))
    print(f'demo1 {num}')
    return num


def demo2():
    num = demo1()
    print(f'demo2 {num}')
    return num


try:
    num = demo2()
    print(f'主流程 {num}')
except Exception as e:
    print(e)
