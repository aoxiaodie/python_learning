from collections import Counter


# 查找列表中出现次数最多的元素
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
# 查找出现频率最高的2个元素
print(word_counts.most_common(2))

# Counter对象是个字典
for word in words:
    word_counts[word] += 1

print(word_counts['eyes'])
# 16，翻倍

print(Counter(words))

# 运算
more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
print()
