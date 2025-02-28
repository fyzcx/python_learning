# 作者: 余畅
# 2025年02月18日15时39分47秒
# fyzcxfyzcx@gmail.com
info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 1. 取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.index("zhangsan"))

# 2. 统计计数
print(info_tuple.count("zhangsan"))
# 统计元组中包含元素的个数
print(len(info_tuple))

print('-'*50)
for i in info_tuple:
    print(i)

info_tuple = ("小明", 21, 1.85)

# 格式化字符串后面的 `()` 本质上就是元组
# print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
info_str1="{} 年龄是 {} 身高是 {}".format(*info_tuple)
print(info_str)
print(info_str1)

# list=[1,2,3]  命名不可以和内置类，内置函数名重名
# list((3,4,5))

