import numpy as np  # as后是别名，别名是短的，提高编写效率
import my_module as m
from my_module import say_hello #高频的使用，用from
from my_module1 import say_hello as say_hello1 #当不同模块中有相同的函数名时，通过as命名别名
import random
# m.say_hello() # 调用模块中的函数

say_hello()
say_hello1()

#想知道模块的路径
print(random.__file__)