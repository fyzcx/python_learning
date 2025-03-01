def swap():
    a = 1
    b = 2
    a, b = b, a
    print(a, b)


def return_more():
    return 1, 2  # 当你返回多个值，是以元组形式返回的


# ret = return_more()
# print(ret)
# print(type(ret))
#
# ret1, ret2 = return_more()
# print(ret1, ret2)

def print_info(name, gender=True):
    """
    缺省参数，简单来说就是形参有默认值，当不给它传递实参时，它就使用默认值
    :param name:
    :param gender:
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


print_info('小明', False)


def print_info2(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s%s 是 %s" % (title, name, gender_text))


# keyword参数
print_info2('小明', gender=False)
