# 作者: 余畅
# 2025年02月18日14时58分14秒
# fyzcxfyzcx@gmail.com


num_list = [x for x in range(10)]

print(num_list)

print('-' * 50)
# 2个for循环
a = [j for i in range(10) for j in range(i)]
print(a)
print('-' * 50)
a = [[col * row for col in range(5)] for row in range(5)]
print(a)
print('-' * 50)

b = [i for j in a for i in j]
print(b)

print('-' * 50)
c = [x for x in range(10) if x % 2 == 0]
print(c)

# if-else的三元表达式
a = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(a)
