import re

# 添加|
ret = re.match(r"[1-9]?\d$|100$", "100")
print(ret.group())

# 匹配163,126，qq邮箱
email_list = ["xiaoWang@163.com", "xiaoWang@126.com", "xiaoWang@163.comheihei", "xiaowang@qq.com"]
for email in email_list:
    ret = re.match(r'\w{5,20}@(163|126|qq)\.com$', email)
    if ret:
        print(f'{email} 是合法的邮箱')
    else:
        print(f'{email} 不是合法的邮箱')

print('-' * 50)
# ([^-]*) 代表没有遇到小横杠-就一直进行匹配，一直匹配下去
ret = re.match(r"([^-]+)-(\d+)", "010-12345678")
if ret:
    # print(ret.group(0))
    print(ret.group(1))
    print(ret.group(2))

# 学习引用分组
# 通过引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
print(ret.group())

labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]

for label in labels:
    ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)

for label in labels:
    ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)
