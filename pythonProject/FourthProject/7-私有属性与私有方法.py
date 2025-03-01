class Women:
    def __init__(self, name, age):
        """
        方法名字不可以改变，用于初始化对象属性的
        :param name:
        :param age:
        """
        self.name = name
        self.__age = age  # 私有属性，只能在类内部访问

    def __secret(self):  # 私有方法，只能在类内部访问,__开头，不能被实例化
        print(self.__age)

    def boy_friend(self):
        self.__secret()


if __name__ == '__main__':
    xiaohong = Women('小红', 18)
    xiaohong.boy_friend()
