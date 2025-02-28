# 作者: 余畅
# 2025年02月18日09时53分54秒
# fyzcxfyzcx@gmail.com

name = 'python程序员'


def print_line(char, nums):
    print(char * nums)
    # print(char1)  #用了不符合一切皆模块的设计原则


if __name__ == '__main__':
    # 测试本模块功能的代码，都需要写在if  __name__ == '__main__ 下面
    char1 = '*'  # 是全局变量
    nums1 = 60
    print_line(char1, nums1)
