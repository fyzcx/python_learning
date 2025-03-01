list1 = [1, 3, 2, 4, 5, 3, 2]

print(sorted(list1))  # sorted是返回一个新的有序列表
print(list1)
# list1.sort()
# print(list1)

print(sorted({1: 'D', 2: 'B', 3: 'B', 5: 'E', 4: 'A'}))
print('-' * 50)
str_list = "This is a test string from Andrew".split()
print(str_list)


# print(sorted(str_list))


def str_lower(str1: str):
    """
    比较规则函数
    :param str1:
    :return:
    """
    return str1.lower()


# str_lower函数是sorted内部进行调用的
print(sorted(str_list, key=str_lower))
print(sorted(str_list, key=str.lower))
print('-' * 50)
# shift+alt 是竖选
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# 匿名函数：函数在当前位置只使用一次，不需要再其他地方再次调用，就会使用匿名函数
# lambda 表达式就是匿名函数
# 匿名函数提升了代码的阅读效率
print(sorted(student_tuples, key=lambda x: x[2]))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        """
        一般str和repr不同时用
        :return:
        """
        return self.name

    def __repr__(self):
        """
        类似str，repr可以返回其他类型(元组类型
        :return:
        """
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

# s = Student('john', 'A', 15)
# print(s)

# 排序对象
print(sorted(student_objects, key=lambda student: student.age))
print('-' * 50)
from operator import itemgetter, attrgetter

print(sorted(student_tuples, key=itemgetter(2)))  # 用于元组或者列表
print(sorted(student_objects, key=attrgetter('age')))  # 用于对象

print('-' * 50)
print(sorted(student_tuples, key=itemgetter(1, 2)))
print(sorted(student_tuples, key=lambda x: x[1:]))

print(sorted(student_objects, key=attrgetter('grade', 'age'), reverse=True))
print(sorted(student_objects, key=lambda student: (student.grade, student.age), reverse=True))

# 感受排序的稳定性
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=lambda x: x[0]))
print('-' * 50)
# 字典嵌套列表
mydict = {'Li': ['M', 7],
          'Zhang': ['E', 2],
          'Wang': ['P', 3],
          'Du': ['C', 2],
          'Ma': ['C', 9],
          'Zhe': ['H', 7]}

# for v in mydict.items():
#     print(v)
print(sorted(mydict.items(), key=lambda v:v[1][1]))


game_result = [
    { "name":"Bob", "wins":10, "losses":3, "rating":75.00 },
    { "name":"David", "wins":3, "losses":5, "rating":57.00 },
    { "name":"Carol", "wins":4, "losses":5, "rating":57.00 },
    { "name":"Patty", "wins":9, "losses":3, "rating": 71.48 }]

print(sorted(game_result,key=itemgetter('rating','name')))

#定义要排序的元组列表
tuples=[(3,5),(1,2),(2,4),(3,1),(1,3)]

#使用sorted函数进行排序，结合lambda表达式定义排序规则
sorted_tuples=sorted(tuples,key=lambda x:(x[0],-x[1]))
print(sorted_tuples)