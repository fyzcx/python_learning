import os


def open_rb():
    """
    以二进制模式打开，读出来的内容是字节流
    字节流不可以加encoding参数
    :return:
    """
    file = open('Python10就业.png', 'rb')
    file1 = open('Python10就业[副本].png', 'wb')
    content_bytes = file.read()
    file1.write(content_bytes)
    file.close()
    file1.close()


def use_seek():
    """
    改变位置指针
    :return:
    """
    file = open('file1', 'rb+', encoding='utf8')
    file.seek(5, os.SEEK_SET)  # 5是改变位置指针多少个字节
    txt = file.read()
    print(txt)
    file.close()


def use_seek_w():
    """
    seek和w+的使用
    :return:
    """
    file = open('file2', 'w+', encoding='utf8')
    file.write('howareyou')
    file.seek(0, os.SEEK_SET)  # 光标回到开头
    txt = file.read()
    print(txt)
    file.close()


if __name__ == '__main__':
    # open_rb()
    use_seek()
    # use_seek_w()
