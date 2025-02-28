# 作者: 余畅
# 2025年02月18日15时33分00秒
# fyzcxfyzcx@gmail.com
a = [1, 2, 3, 4, 5]
b = [2, 3, 4]
c=[0]*10

print(id(a))
# print(a * 2)
# print(a + b)
# print(c)
a += b  # 等价于extend ,和a=a+b是不一样的
print(a)
print(id(a))