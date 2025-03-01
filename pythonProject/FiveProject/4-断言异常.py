def input_password():
    """
    自定义异常并抛出
    :return:
    """
    password = input('请输入密码')
    assert len(password) >= 8, '此处发生了什么什么异常'  # 自定义异常并抛出, 断言密码长度必须大于等于8
    return password


try:
    password = input_password()
    print(password)
except Exception as e:
    print(f'e的信息 {e}')
