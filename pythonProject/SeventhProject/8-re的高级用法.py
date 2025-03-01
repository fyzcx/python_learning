# search，findall，sub，split

import re

ret = re.search(r"\d+", "阅读次数为 9999,点赞数888，收藏666")
print(ret.group())


def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)  # matches是一个迭代器
    try:
        next(matches)  # 跳过第一个匹配项
        next(matches)
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None


text = "abc123def456ghi789"
pattern = r"\d+"
second_match = find_second_match(pattern, text)
print(second_match)
print('-' * 50)
ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)  # 返回是列表类型

print('-' * 50)


def add(match_result):
    """
    返回值一定要是字符串
    :param match_result: 匹配后的match对象
    :return:
    """
    return str(int(match_result.group()) + 1)


ret = re.sub(r'\d+', '998', '阅读量997')
print(ret)  # 返回的是替换后的字符串


ret = re.sub(r'\d+', add, '阅读量666')
print(ret)


text = "apple apple apple apple"
pattern = r"apple"
replacement = "orange"

new_text = re.sub(pattern, replacement, text,count=2)
print(new_text)

print('-'*50)
s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
ret_s = re.sub(r'年|月', r'/', s)
ret_s = re.sub(r'日', r' ', ret_s)
ret_s = re.sub(r'时|分', r':', ret_s)
print(ret_s)
# findall 有问题
com = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
ret = com.findall(ret_s)
print(ret)