class Animal:
    def eat(self):
        print('eat')

    def drink(self):
        print('drink')

    def run(self):
        print('run')

    def sleep(self):
        print('sleep')


class Dog(Animal):  # 单继承
    def bark(self):
        print('bark')


class Cat(Animal):
    def catch(self):
        print('catch')


class XiaoTianQuan(Dog):
    def fly(self):
        print('fly')

    def bark(self):
        super().bark()  # 调用父类中bark方法
        print('像神一样叫')


if __name__ == '__main__':
    wangcai = Dog()
    wangcai.eat()
    wangcai.drink()
    print('-' * 50)
    xiaotianquan = XiaoTianQuan()
    xiaotianquan.bark()
