class A:
    def test(self):
        print("A.test()")


class B:
    def test(self):
        print("B.test()")

    def demo(self):
        print('B demo')


class C(A, B):  # 多重继承, 先继承A, 再继承B, 后定义C, 所以C的mro为(C, A, B, object)
    def test(self):
        super().test()
        print('c test()')


if __name__ == '__main__':
    c = C()
    c.test()
    print(C.__mro__)
    c.demo()
