import os  # 导入os模块,用于文件操作,路径操作,系统调用等


def use_open_r():
    file = open('file1', 'r', encoding='utf8')
    txt = file.read()
    print(txt)
    file.close()


def use_open_rw():
    """
    使用r+
    :return:
    """
    file = open('file1', 'r+', encoding='utf8')
    nums = file.write('HELLO')  # nums表示写入的字符数
    print(nums)
    file.close()


def use_open_a():
    """
    使用a，以追加方式写入
    :return:
    """
    file = open('file1', 'a', encoding='utf8')
    nums = file.write('HELLO')  # nums表示写入的字符数
    print(nums)
    file.close()


def use_open_w():
    """
    w方式 文件不存在会创建，存在了，就会被清空
    / 路径  非常推荐
    \\  反斜杠用两个\\
    绝对路径  windows从盘符开始的，mac和Linux都是/ 开头，就是绝对路径
    相对路径   相对于当前进程的路径, 写代码，大家都会用相对路径
    :return:
    """
    file = open('dir1/dir2/file3.txt', 'w', encoding='utf8')
    print(os.getcwd())  # 查看当前进程的路径
    file.write('howareyou')
    file.close()


def use_readline():
    """
    每次都一行,直到把文件读完
    :return:
    """
    file = open('file1', 'r+', encoding='utf8')
    while True:
        txt = file.readline()
        if not txt:
            break
        print(txt,end='')


if __name__ == '__main__':
    # use_open_r()
    # use_open_rw()
    # use_open_a()
    # use_open_w()
    use_readline()