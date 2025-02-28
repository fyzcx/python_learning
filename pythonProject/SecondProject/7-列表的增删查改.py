# 作者: 余畅
# 2025年02月18日14时17分18秒
# fyzcxfyzcx@gmail.com


name_list = ["zhangsan", "lisi", "wangwu"]
print(f'id(name_list)={id(name_list)}')
# 查
# 1. 取值和取索引
# list index out of range - 列表索引超出范围
print(name_list[2])
print(name_list.index('wangwu'))

# 2.修改
print('-'*60)
name_list[1] = 10
print(name_list)
# 列表指定的索引超出范围，程序会报错！


#3.增加
print('-'*60)
name_list.append('王小二')
print(name_list)
# insert 方法可以在列表的指定索引位置插入数据
name_list.insert(0,'王小美')
print(name_list)
# extend 方法可以把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)
print(name_list)
print(f'id(name_list)={id(name_list)}')

# 4. 删除
print('-'*60)
# remove 方法可以从列表中删除指定的数据
name_list.remove("wangwu")
print(name_list)
name_list.pop(2)
print(name_list)
del name_list[1]
print(name_list)
# clear 方法可以清空列表
name_list.clear()
print(name_list)
print(f'clear之后 id(name_list)={id(name_list)}')