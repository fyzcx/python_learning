a = (1, 2, 3)
b = ('a', 'b', 'c')

print(list(zip(a, b)))  # 对应位置进行组合

ab_dict = {v: k for k, v in list(zip(a, b))}
print(ab_dict)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

for id, val in enumerate(seasons):
    print(id, val)

my_dict = {val: id for id, val in enumerate(seasons)}
print(my_dict)
