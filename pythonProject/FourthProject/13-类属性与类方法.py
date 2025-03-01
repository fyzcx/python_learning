class Tool:
    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod  # 定义类方法, 类方法的第一个参数必须是cls, 代表类本身, 而不是实例对象,, 类方法可以访问类属性, 但不能访问实例属性
    def show_tool_count(cls):  # cls是类名
        """显示工具对象的总数"""
        print("工具对象的总数 %d" % cls.count)

    @staticmethod  # 定义静态方法, 静态方法不需要实例化, 也不需要访问类属性, 但可以访问实例属性, 类属性
    def help():
        print('游戏帮助')


if __name__ == '__main__':
    # 创建工具对象
    tool1 = Tool("斧头")
    tool2 = Tool("榔头")
    tool3 = Tool("铁锹")
    print(Tool.count)
    # tool3.count = 99  # 增加了一个对象属性
    # print("工具对象总数 %d" % tool3.count)
    # print("===> %d" % Tool.count)
    Tool.show_tool_count()
    print(Tool)
    Tool.help()
