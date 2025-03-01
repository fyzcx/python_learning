def use_except():
    """
    练习简单的异常捕获
    :return:
    """
    while True:
        try:
            num = int(input('请输入一个数字:'))
            print(num)
            break
        except:
            print('请输入数字')


def use_except_more_type():
    """
    使用不同的异常类型
    :return:
    """
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print('请输入整数')
    except ZeroDivisionError:
        print('不可以输入0')
    except Exception as result:
        print(result)


def use_else_finally():
    """
    使用else和finally，用的比较少
    :return:
    """
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
        return None
        print('哈哈，你看不到我') # 不会执行
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
    except Exception as result:
        print("未知错误 %s" % result)
    else:
        print("正常执行")
    finally:  # 不受return影响
        print("执行完成，但是不保证正确")


if __name__ == '__main__':
    # use_except()
    # use_except_more_type()
    use_else_finally()
