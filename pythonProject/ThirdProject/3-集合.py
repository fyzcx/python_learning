
def use_set():
    my_set = set()  # 如何初始化空集合
    print(my_set)
    print(type(my_set))

    my_set = {"apple", "banana", "cherry"}
    print('apple' in my_set)


def use_copy():
    a = [1, 2, 3]
    b = a
    print(f'id(a)={id(a)},id(b)={id(b)}')
    a[0] = 5
    print(b)


def use_set_sym():
    """
    练习集合的快捷操作
    :return:
    """
    a = set('abracadabra')
    b = set('alacazam')
    print(a, b)
    print(a - b)  # difference
    print(a | b)  # 并集
    print(a & b)  # 交集
    print(a ^ b)  # 并集-交集


# use_copy()
use_set_sym()
print(type(1))