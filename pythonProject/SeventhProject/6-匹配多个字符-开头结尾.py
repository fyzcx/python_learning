import re

ret = re.match("[A-Z][a-z]*", "M")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "MnnM")
print(ret.group())

ret = re.match("[A-Z][a-z]*", "Aabcdef")
print(ret.group())

print('-' * 50)
# 匹配变量名是否合法
names = ["name1", "_name", "2_name", "__name__"]
for name in names:
    ret = re.match(r'[a-zA-Z_]\w*', name)
    if ret:
        print(f'{ret.group()} 是合法的变量名')
    else:
        print(f'{name} 不是合法的变量名')
print('-' * 50)
# 匹配0-99是否合法
ret = re.match(r"[1-9]?[0-9]", "7")
print(ret.group())

ret = re.match(r"[1-9]?\d", "33")
print(ret.group())

ret = re.match(r"[1-9]?\d$", "9")
if ret:
    print(ret.group())
else:
    print('数字不合法')

# 匹配{m}
ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
print(ret.group())

# 默认是贪婪的
ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s34455ff66")
print(ret.group())

print('-' * 50)
# 匹配邮箱地址
email_list = ["xiaoWang@163.com", "xiaoWang@1636com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for email in email_list:
    ret = re.match(r'\w{5,20}@163\.com$', email)
    if ret:
        print(f'{email} 是合法的邮箱')
    else:
        print(f'{email} 不是合法的邮箱')
