class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('eat')

    def drink(self):
        print('drink')

    def run(self):
        print('run')

    def sleep(self):
        print('sleep')


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def bark(self):
        print('bark')


class XiaoTianQuan(Dog):
    def __init__(self, name, color, weapon):
        super().__init__(name, color)
        self.weapon = weapon

    def fly(self):
        print('fly')


if __name__ == '__main__':
    dog = Dog('大黄', '黄色')
    print(dog.name)
    print(dog.color)
    xiaotianquan = XiaoTianQuan('哮天犬', '黑色', '翅膀')
    print(xiaotianquan.name)
