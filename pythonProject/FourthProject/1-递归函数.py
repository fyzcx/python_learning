import sys

sys.setrecursionlimit(20000)


def f(n):
    if n == 1:  # 结束条件写到return之前
        return 1
    return n + f(n - 1)


n = int(input('请输入一个值：'))
print(f(n))


def step(n):
    if n == 1 or n == 2:
        return n
    return step(n - 1) + step(n - 2)
# while True:
#     n = int(input('请输入台阶数目：'))
#     print(step(n))
