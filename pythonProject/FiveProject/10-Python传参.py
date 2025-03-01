import sys  # 导入sys模块,用于获取命令行参数,以及读写文件


# argv是一个列表
# print(sys.argv)

def use_argv():
    """
    根据传递的参数不同，打开不同的文件，读取内容并打印
    :return:
    """
    file = open(sys.argv[1], 'r', encoding='utf8')
    print(file.read())
    file.close()


use_argv()
