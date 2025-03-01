# eval的作用是把字符串内的内容，作为代码来执行
print(eval('1+1'))


# os.system() Python 嵌入别的语言

def read_conf():
    """
    读取配置专用
    :return:
    """
    file = open('file3', 'r', encoding='utf8')
    txt = file.read()
    conf_dict = eval(txt)  # 把字符串变为一个字典
    print(type(conf_dict))
    print(conf_dict)
    file.close()


if __name__ == '__main__':
    read_conf()
