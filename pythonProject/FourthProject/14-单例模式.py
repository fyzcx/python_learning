# class MusicPlayer(object):
#     def __new__(cls, *args, **kwargs):
#         # 1. 创建对象时，new方法会被自动调用
#         print("创建对象，分配空间")
#         # 2. 为对应的对象分配空间
#         instance = super().__new__(cls)
#         # 3.返回
#         return instance
#
#     def __init__(self):
#         print("播放器初始化")


class MusicPlayer(object):
    """
    单例模式，第二次是实例化时，得到的对象仍然和第一次相同
    """
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:  # 判断是否申请过空间了
            cls.instance = super().__new__(cls)
        # 3.返回
        return cls.instance

    def __init__(self,music_name):
        print(f"播放器初始化{music_name}")
        self.music_name=music_name


if __name__ == '__main__':
    player1 = MusicPlayer('七里香')
    player2 = MusicPlayer('东风破')
    print(id(player1))
    print(id(player2))
