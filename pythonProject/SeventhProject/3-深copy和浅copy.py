import copy


def use_copy():
    a = [12, 22]
    b = [33, 44]
    c = copy.copy(a)  # copy.copy 是浅copy，主要是复制自定义对象
    print(c)
    a[0] = 50
    print(c)


def use_deepcopy():
    a = [12, 22]
    b = [33, 44]
    c = [a, b]
    d = copy.deepcopy(c)  # 递归的进行copy，直到不可变数据类型
    # d=c.copy()  #列表的copy是浅copy
    print(f'id(c)={id(c)},id(d)={id(d)}')
    print(f'id(c[0])={id(c[0])},id(d[0])={id(d[0])}')
    print(d)
    a[0] = 50
    print(d)


# 自定义对象，对象内有一个属性，这个属性又是另外一个对象
if __name__ == '__main__':
    use_deepcopy()
