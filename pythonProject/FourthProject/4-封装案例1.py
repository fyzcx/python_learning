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

    def __str__(self):
        return f'{self.name} 现在体重是{self.weight}'


# elephant = Person('大象', 18, 80)
# elephant.run()
# elephant.eat()
# print(elephant)
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area  # 剩余面积
        self.item_list = []  # 家具列表

    def add_item(self, item: HouseItem):  # 冒号:类名是注解的作用，协助写代码的
        print(f'要添加 {item}')
        if self.free_area >= item.area:
            self.item_list.append(item.name)
            self.free_area -= item.area
        else:
            print('房间空间不足')

    def __str__(self):

        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))


# 1. 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

# print(bed)
# print(chest)
# print(table)
house = House('三室一厅', 70)
print(house)
house.add_item(bed)
house.add_item(table)
print(house)
