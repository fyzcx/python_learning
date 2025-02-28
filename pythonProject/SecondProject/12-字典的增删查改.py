# 作者: 余畅
# 2025年02月18日15时56分28秒
# fyzcxfyzcx@gmail.com


def use_dict():
    """
    字典的增删查改
    :return:
    """
    xiaoming_dict = {"name": "小明"}

    print(f'最初的id={id(xiaoming_dict)}')
    # 1. 取值
    print(xiaoming_dict["name"])
    # 在取值的时候，如果指定的key不存在，程序会报错！
    # print(xiaoming_dict["name123"])
    print(xiaoming_dict.get('name123'))

    # 2. 增加/修改
    # 如果key不存在，会新增键值对
    xiaoming_dict["age"] = 18
    # 如果key存在，会修改已经存在的键值对
    # xiaoming_dict.setdefault('name','小小明')
    xiaoming_dict["name"] = "小小明"
    print(f'xiaoming_dict={xiaoming_dict},id(xiaoming_dict)={id(xiaoming_dict)}')

    # 3.删除
    # xiaoming_dict.pop('name')
    print(xiaoming_dict)

    print('-' * 50)
    xiaoming_dict = {"name": "小明",
                     "age": 18}

    # 1.统计长度
    print(len(xiaoming_dict))
    # 2. 合并字典
    temp_dict = {"height": 1.75,
                 "age": 20}

    # 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
    xiaoming_dict.update(temp_dict)

    # 3. 清空字典
    # xiaoming_dict.clear()

    print(xiaoming_dict)


def use_dict_iter():
    xiaoming_dict = {"name": "小明",
                     "qq": "123456",
                     "phone": "10086"}
    for key in xiaoming_dict:
        print(key)
    print('-' * 50)
    for v in xiaoming_dict.values():
        print(v)
    print('-' * 50)
    for k, v in xiaoming_dict.items():
        print(k, v)

def use_list_dict():
    """
    列表嵌套字典
    :return:
    """
    card_list = [
        {"name": "张三",
         "qq": "12345",
         "phone": "110"},
        {"name": "李四",
         "qq": "54321",
         "phone": "10086"}
    ]
    for card in card_list:
        for k,v in card.items():
            print(k,v)
        print('-' * 50)

use_dict()
# use_dict_iter()
# use_list_dict()
