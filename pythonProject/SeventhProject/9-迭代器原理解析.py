# 把range(10)换掉变为自己的

for i in range(10):
    print(i, end=' ')


# 迭代器----》生成器
def f(n):
    i = 0
    while i < n:
        yield i  # 让进程暂停到这个位置，并i返回
        i += 1
    return


print()
for j in f(10):
    print(j, end=' ')

print('\n-----------------------')
myiter = f(2)
print(next(myiter))
print(next(myiter))
# print(next(myiter))
# print(next(myiter))

for i in myiter:
    print(i)
print('\n-----------------------')
for i in myiter:
    print(i)

# mylist=[1,2,3] 可迭代对象   迭代器
# for i in mylist:
#     print(i)
# for i in mylist:
#     print(i)
