import re

result=re.match('wangdao','wangdao.cn')
if result:
    print(result.group())


ret = re.match(".","M")
print(ret.group())

ret = re.match("t.o","too")
print(ret.group())

ret = re.match("t.o","two")
print(ret.group())

print('-'*50)
# 大小写h都可以的情况
ret = re.match("[hH]","hello Python")
print(ret.group())
ret = re.match("[hH]","Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python","Hello Python")
print(ret.group())
print('-'*50)
# 匹配0到9第二种写法
ret = re.match("[0-9]Hello Python","7Hello Python")
print(ret.group())

ret = re.match("[0-35-9]Hello Python","7Hello Python")
print(ret.group())

print('-'*50)
# 使用\d进行匹配
print(f'使用\\d进行匹配')
ret = re.match(r"嫦娥\d号","嫦娥1号发射成功")
print(ret.group())

ret = re.match(r"嫦娥\d号","嫦娥2号发射成功")
print(ret.group())

ret = re.match(r"嫦娥\d号","嫦娥3号发射成功")
print(ret.group())