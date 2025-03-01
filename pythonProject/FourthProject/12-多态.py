class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog: Dog):  # 这里的Dog是父类，Dog的子类XiaoTianDog也能被传入, 这就是多态, 父类引用指向子类对象，调用子类的方法, 得到不同的结果
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        dog.game()  # 不同的对象，执行相同的方法，得到了不同的行为   ---这就是多态


if __name__ == '__main__':
    wangcai = Dog('旺财')
    wangcai1 = Dog('旺财1号')
    xiaotianquan = XiaoTianDog('哮天犬')
    xiaoming = Person('小明')
    xiaoming.game_with_dog(wangcai)
    print('-' * 50)
    xiaoming.game_with_dog(xiaotianquan)
