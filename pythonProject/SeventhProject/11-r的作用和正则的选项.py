import re
mm = "c:\\a\\b\\c"
print(mm)

print(re.match(r"c:\\",mm).group())

text = "Hello 世界 123"
pattern = r"\w+"

# 使用 re.A 标志，\w 只匹配 ASCII 字符（不匹配汉字）
result = re.findall(pattern, text, flags=re.A)
print(result)  # 输出: ['Hello', '123']

text = "Hello World hello world"
pattern = r"hello"

# 使用 re.I 标志，不区分大小写
result = re.findall(pattern, text, flags=re.I)
print(result)  # 输出: ['Hello', 'hello']

text = "Hello\nWorld"
pattern = r"Hello.World"

# 使用 re.S 标志，. 可以匹配 \n
result = re.findall(pattern, text, flags=re.S)
print(result)  # 输出: ['Hello\nWorld']