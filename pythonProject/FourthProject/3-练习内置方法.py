class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        """
        用于记录对象被销毁的日志
        :return:
        """
        print("%s 我去了" % self.name)

    def __str__(self):
        """
        需要返回字符串类型，打印对象时，得到的就是这个函数的返回值
        :return:
        """
        return self.name


tom = Cat('Tom')
print(f'打印对象 {tom}')

del tom
print('程序结束')
