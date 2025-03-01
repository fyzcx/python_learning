def input_password():
    """
    自定义异常并抛出
    :return:
    """
    password=input('请输入密码')
    if len(password)>=8:
        return password

    raise Exception('密码长度要大于等于8位')


try:
    password=input_password()
    print(password)
except Exception as e:
    print(f'e的信息 {e}')