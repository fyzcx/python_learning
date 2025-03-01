def print_exception_pos(e):
    """
    打印异常位置
    :return:
    """
    print(e)
    print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件, 即__file__变量的值
    print(e.__traceback__.tb_lineno)  # 发生异常所在的行数


try:
    a = 1 / 0
except Exception as e:
    print_exception_pos(e)
