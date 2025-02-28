# 作者: 余畅
# 2025年02月18日14时37分15秒
# fyzcxfyzcx@gmail.com

def use_len_count():
    name_list = ["张三", "李四", "王五", "王小二", "张三"]

    # len(length 长度) 函数可以统计列表中元素的总数
    print(len(name_list))

    print(name_list.count('张三'))

    # name_list.remove('lele') #如果要删除的值不在列表，会抛异常


def use_sort():
    """
    使用排序
    :return:
    """
    name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
    num_list = [6, 8, 4, 1, 10]

    name_list.sort()
    num_list.sort(reverse=True)

    print(name_list)
    print(num_list)


def use_reverse():
    name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
    num_list = [6, 8, 4, 1, 10]

    # 逆序（反转）
    name_list.reverse()
    num_list.reverse()

    print(name_list)
    print(num_list)


def use_iter():
    """
    练习遍历
    :return:
    """
    name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
    for name in name_list:
        print(name, end=' ')
    print()
    i = 0
    while i < len(name_list):  # 删除列表中的元素时，用while遍历
        print(name_list[i], end=' ')
        i += 1
    print()


# use_sort()
# use_reverse()
use_iter()
