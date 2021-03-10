from collections import deque

# 添加
# 从右边添加
d = deque()
d.append(1)
d.append(2)
print(d)
# deque([1, 2])

# 从左边添加
d.appendleft(0)
print(d)
# deque([0, 1, 2])

# 判断是否存在
q = deque([1, 2, 3, 4])
print(5 in q)
# false
print(1 in q)
# true

# 将整个队列旋转
# 顺时针旋转
q.rotate(1)
print(q)
# deque([4, 1, 2, 3])

# 逆时针旋转
q.rotate(-1)
print(q)
# deque([1, 2, 3, 4])

# 获取指定元素出现的个数
print(q.count(2))
# 1

# 添加列表
# 从右边一个列表
q.extend(d)
print(q)
# deque([1, 2, 3, 4, 0, 1, 2])

# 从做边一个列表
q.extendleft(d)
print(q)
# deque([0, 1, 2, 1, 2, 3, 4, 0, 1, 2])

# 查找某个元素的索引位置
print(q.index(4))
# 6

# 如果有重复，则找到第一个
print(q.index(1))
# 1

# 在区间内查找
print(q.index(1, 2, 4))
# 3

# 在指定位置插入
q.insert(0, 100)
print(q)
# deque([100, 2, 1, 0, 1, 2, 3, 4, 0, 1, 2])

# 删除指定元素，存在多个时，仅删除第一个
q.remove(2)
print(q)
# deque([100, 1, 0, 1, 2, 3, 4, 0, 1, 2])

# pop最右的元素
q.pop()
print(q)
# deque([100, 2, 1, 0, 1, 2, 3, 4, 0, 1])

# pop最左的元素
q.popleft()
print(q)
# deque([2, 1, 0, 1, 2, 3, 4, 0, 1])

# 清空
q.clear()
print(q)
