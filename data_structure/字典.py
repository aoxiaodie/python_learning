from collections import defaultdict, OrderedDict


# （1）映射多个值
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(d)
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})

# （2）字典排序
c = OrderedDict()
c['name'] = "vae"
c['age'] = 30
c['phone_number'] = 520
for key in c:
    print(key, c[key])
# name
# vae
# age
# 30
# phone_number
# 520

e = dict()
e['name'] = "vae"
e['age'] = 30
e['phone_number'] = 520
for key in e:
    print(key, e[key])

# （3）字典运算
# zip可将字典的key、value翻转
prices = {
    'ACME': 45.23,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
sorted_price = sorted(zip(prices.values(), prices.keys()))
print(sorted_price)

# （4）查询字典的相同值
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'x': 22,
    'y': 2,
    'w': 44
}

# 找到相同的key
print(a.keys() & b.keys())

# 找到在a但不在b的key
print(a.keys() - b.keys())

# 找到相同的(key, values)
print(a.items() & b.items())
