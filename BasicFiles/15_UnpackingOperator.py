# 当我们创建一个列表的时候，如果直接输出则只会输出整个列表
# 但是如果我们想要输出列表内的元素，我们就需要解包
from pprint import pprint

values = [1, 2, 3, 4, 5]
print(values)  # 输出整个列表
print(*values)  # 解包输出列表内的元素
# Python中的解包操作是一个*，在JS中是...
# 比如上面这个列表，解包后和下面的输出是一致的
print(1, 2, 3, 4, 5)
# 一般创建这种列表我们使用range函数，它返回的是range对象，我们再用List函数转换一下即可
values = list(range(1, 6))
print(values)  # 输出整个列表
print(*values)  # 解包输出列表内的元素
# 实际上解包符号能适用在任何可迭代对象上
values = [*range(5), *"Hello"]
print(values)  # 输出整个列表
print(*values)  # 解包输出列表内的元素
# 这种方便的解包操作只有Python独有，在其他语言中是没有的

# 解包操作可以应用到字典中，只需要记得由于字典是键值对，所以我们要用两个*符号解包
first_dict = {"a": 1, "b": 2}
second_dict = {"a": 5, "c": 3, "d": 4}
# 解包字典时，使用两个*符号
combined_dict = {**first_dict, **second_dict, "z": 9}
print(combined_dict)  # 输出合并后的字典
# {'a': 5, 'b': 2, 'c': 3, 'd': 4, 'z': 9}
# 可以看到当出现相同键的时候，后面的字典会覆盖前面的字典中的键值对

# Exercise:统计出下面字符串中重复次数最多的字母
# 从以往编程语言的经验中，很容易想到下面这样的解法
sentence = "This is a common interview question"
count = 0
letter = "a"
for x in sentence:
    if count < sentence.count(x):
        count = sentence.count(x)
        letter = x
print(letter, count)
# 但是为了尽可能多地使用我们学到的知识，我们可以这样做
# 首先应该想到的就是如何存储 字母+次数 这种数据
# 显然，字典是一个好选择
# 于是我们首先创建一个空字典
sentence = "This is a common interview question"
char_frequency = {}
# 接下来我们需要统计sentence中的所有字符以及它的出现次数，并放到字典里
for char in sentence:
    # 当char存在于字典中时，我们只需要给它对应的值+1即可
    if char in char_frequency:
        # 既然char在字典里，那就可以通过char_frequency[char]来访问它对应的值了，然后给它+1即可
        char_frequency[char] += 1
    else:
        # 当字典中不存在这个字符时，我们需要把它放到字典中，并给它的值赋1
        char_frequency[char] = 1
# 这样我们就取到了句子中所有字母以及它的出现次数的键值对,为了方便展示，我们引入了pprint模块来美化输出
pprint(char_frequency, width=1)  # 单列输出字典
# 接下来我们只要将整个字典排序，把频率最高的字母放到第一位，然后取出它就可以了
# 问题是字典是不能排序的，所以我们首先要把字典进行转换，拥有键值对还能排序
# 但是不可能直接将字典放到元组中，我们需要将每个键值对做成一个元组，然后放到一个数据结构中
# 也就是说，首先将字典的键值对做成元组，然后把所有元组放到一个列表中，再排序
# 还记得字典的items()方法吗，它会将字典做成一个包含每个键值对作为单元组的列表，正好符合我们的需求
# 于是第一步，就是 char_frequency.items()，它会返回一个包含每个键值对作为单元组的列表
print(char_frequency.items())
# 对于列表的排序，刚刚好就需要用到sorted()函数，首先传入一个可迭代对象，刚刚生成的列表就是这个参数
# 然后需要告诉sorted函数按照什么来排序，我们需要按照每个元组的第二个元素来排序，也就是频率
# 所以我们需要一个lambda函数来告诉sorted函数按照每个元组的第二个元素来排序
# 这里使用lambda函数的原因是我们不想单独定义一个函数来告诉sorted函数按照什么来排序，我们只想在这里告诉它一次就好了
# kv是每个元组，kv[1]就是每个元组的第二个元素，正好也就是频率
# sorted()方法排序的结果是从小到大的，但是我们要最大频率的字母，所以我们需要将reverse参数设置为True，这样就是从大到小排序了
# 为了保证代码的可读性，对于长参数pylint会建议将它们放在不同的行上，这样就不会太长，我这里根据屏幕大小，一行也可以，所以没有换行
char_frenquency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True
)
# 当排序完成后，我们只需要从列表中取出第一个元组就可以了，这个元组的第一个元素就是频率最高的字母，第二个元素就是它的频率
print(char_frenquency_sorted[0])  # 输出: ('i', 5)

sentence = "This is a common interview question"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)
print(char_frequency.items())
char_frenquency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True
)
print(char_frenquency_sorted[0])  # 输出: ('i', 5)
