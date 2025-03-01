import os


def use_rename():
    os.rename('dir1/file3.txt', 'dir1/file4.txt')


def use_remove():
    """
    只能删普通文件
    :return:
    """
    os.remove('dir1/file4.txt')


def use_listdir():
    print(os.listdir('..'))


def use_rmdir():
    os.rmdir('dir1')


def use_chdir():
    """
    改变路径
    :return:
    """
    print(os.getcwd())
    os.chdir('dir1')
    file = open('file5.txt', 'w')
    file.close()
    print(os.getcwd())


def scan_dir(path, width):
    """
    深度优先遍历
    :param path:
    :return:
    """
    file_names_list = os.listdir(path)
    for file_name in file_names_list:
        print(' ' * width + file_name)  # 打印名字
        new_path = path + '/' + file_name  # 拼接为正确的路径
        if os.path.isdir(new_path):  # 是文件夹返回True，否则返回False
            scan_dir(new_path, width + 4)  # 每递归一次，往后推4个空格


from time import strftime
from time import gmtime


def use_stat():
    """
    获取文件的信息
    :return:
    """
    file_info = os.stat('file1')
    print('size {},uid{},mtime {}'.format(file_info.st_size, file_info.st_uid,
                                          file_info.st_mtime))

    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime(file_info.st_mtime)))


if __name__ == '__main__':
    # use_rename()
    # use_remove()
    # use_listdir()
    # use_rmdir()
    # use_chdir()
    # scan_dir('.', 0)
    use_stat()
