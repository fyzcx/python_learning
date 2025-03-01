class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f'{self.name}跑步了,体重减少0.5公斤{self.weight}')

    def eat(self):
        self.weight += 1
        print(f'{self.name}吃大餐，体重增加1公斤{self.weight}')


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        pass

    def shake(self):
        pass


if __name__ == '__main__':
    elephant = Person('大象', 18, 80)  # 实例化对象
    tiger = Person('老虎', 17, 60)

    elephant.run()  # 对象调用方法
    elephant.eat()
    print(elephant.weight)
    elephant.height = 1.85  # 编程风格是不规范，大家都不这么写
    print(elephant.height)
    elephant.age=20

    print('-' * 50)
    print(dir(Person))
    print(dir(elephant))

    wangcai = Dog('wangcai', 'yellow')
    wangcai.bark()
