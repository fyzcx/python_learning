# 作者: 余畅
# 2025年02月17日15时53分40秒
# fyzcxfyzcx@gmail.com
import random

def use_if():
    # 1. 定义年龄变量
    age = 18

    # 2. 判断是否满 18 岁
    # if 语句以及缩进部分的代码是一个完整的代码块
    if age >= 18:
        print("可以进网吧嗨皮……")
    else:
        print('不能进网吧')

    # 3. 思考！- 无论条件是否满足都会执行
    print("这句代码什么时候执行?")


def use_elif():
    holiday_name = "平安夜"

    if holiday_name == "情人节":
        print("买玫瑰")
        print("看电影")
    elif holiday_name == "平安夜":
        print("买苹果")
        print("吃大餐")
    elif holiday_name == "生日":
        print("买蛋糕")
    else:
        print("每天都是节日啊……")


def use_random():
    player=int(input('请输入'))
    computer=random.randint(1,3)
    if ((player == 1 and computer == 2) or
            (player == 2 and computer == 3) or
            (player == 3 and computer == 1)):

        print("噢耶！！！电脑弱爆了！！！")
    elif player == computer:
        print("心有灵犀，再来一盘！")
    else:
        print("不行，我要和你决战到天亮！")

# use_elif()
use_random()