"""Python中列表可以存储字符串数值等变量，甚至列表本身也能存储列表"""

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
# 为了创建一个有100个0的列表，不需要用循环也不需要输100次“0”，只需要使用*符号即可实现
# zeros = [0] * 100
# print(zeros)
# 列表之间甚至可以进行拼接，为了便于展示这里重新定义一下zeros列表
zeros = [0] * 5
combined = zeros + letters
print(combined)
# 你可以看到列表中的变量没有类型限制，列表中的每一个位置的变量都可以是不同的类型
# 如果你需要创建一个从1到20的列表，可以直接使用list函数，并传入range函数，从而摆脱循环
numbers = list(range(20))
chars = list("Hello World")
print(numbers)  # 输出从0到20的数，但是不包括20本身
print(chars)  # 字符串被切分为了字母层级，每一个字母均是列表中的一个元素，甚至是空格也是
# 借助len函数可以获取列表的长度
print(len(chars))  # 11

letters = ["a", "b", "c", "d", "e", "f", "g"]
# 列表是有序的，因此可以通过索引来访问列表中的元素
print(letters[0])  # 输出a
print(letters[-1])  # 输出倒数第一个元素，即g
# 通过索引我们可以直接修改列表中的内容
letters[0] = "A"
print(letters)  # 输出["A", "b", "c", "d", "e", "f", "g"]
# 同样的我们也可以使用列表切片，即获取列表中的某一部分，切片的语法是：列表[开始索引:结束索引:步长]
print(letters[0:3])  # 输出["A", "b", "c"]，注意切片的结束索引是不包括的
print(letters[:3])  # 输出["A", "b", "c"]，省略开始索引默认从0开始
print(letters[3:])  # 输出["d", "e", "f", "g"]，省略结束索引默认到列表末尾
print(letters[::2])  # 输出["A", "c", "e", "g"]，步长为2，即每隔一个元素取一个
# 使用步长的意义是，你可以输出每两个/每N个元素，从而实现一些特定的功能，比如每隔一个元素取一个，就可以实现隔行输出
print(numbers[::2])  # 输出从0到20的数，但是不包括20本身，每隔一个元素取一个
# 步长还有个用处是规定输出开头在哪里
print(
    numbers[::-1]
)  # 输出从0到20的数，但是不包括20本身，步长为-1，即从后往前取，因此输出的是倒序

# 当需要取出列表的元素并命名为变量时，Python引出了列表解包操作
# 当我们需要解包列表时，我们没必要一个一个地定义变量去对应列表元素，我们可以使用连续的变量名解包
# first=numbers[0]  # 穷举式地解包过于繁琐
# second=numbers[1]
# third=numbers[2]
# 我们可以直接定义完变量名，然后直接赋值列表，需要注意的是变量个数必须和列表元素个数对应
# first, second, third = numbers # 这样会报数值错误ValueError: too many values to unpack (expected 3)
first, second, third, fourth = numbers[0:4]
print(first, second, third, fourth)  # 输出0 1 2 3
# 但实际上一个列表可能包括很多元素，元素个数也很多，这样我们一个一个地解包是不现实的，因此Python引入了*符号
# *符号可以用来表示剩余的元素，因此我们可以这样解包
first, second, *other = numbers[
    0:5
]  # other不会直接按需求存储变量，但是它会将已解包的元素剔除，并将剩余的元素存在other列表中
print(second)
print(other)  # 输出[2，3, 4]
print(type(other))  # 输出<class 'list'>
# other可以出现在任何位置，但是*只能出现一次，因为*只能代表剩余的元素，不能代表多个剩余的元素
first, *other, last = numbers[0:5]
print(first)
print(other)
print(last)


# 可以看到我们这样就实现了部分元素的解包和剩余元素的打包操作
# 回到之前说的函数定义，*在定义参数时也是这样操作的
def multiply(*numbers):
    """无论给入任何参数，都直接输出内容"""
    # 输入的参数理应会被存为列表，但是由于是在函数里作为参数，所以会是一个元组
    print(type(numbers))  #     <class 'tuple'>
    print(numbers)


multiply(1, 2, 3, 4, 5)
# 这里的1，2，3，4，5会在作为*numbers参数时，自动被打包成元组
# 为什么是元组而不是列表，因为Python官方定义：args收集的参数不应该被修改，相比于列表，显然元组更加稳定
# 所以*应该被看作是将多个参数打包成一个“集合”的符号，只是用来打包/解包的符号，无法决定最终的类型

# 习惯使然，人们经常使用循环对列表解包，但是仅仅提取出列表内元素就有些简单了
# 一般列表内的数据会按照顺序被解包，enumerate函数可以让我们同时获取列表的索引和元素
# enumerate函数只能接收Iterable(可迭代对象)作为参数，因此可以通过for循环遍历
# 可以理解为enumerate函数可以给Iterable里的每个东西自动编号，然后返回一个元组，元组中包含编号和内容
for letter in enumerate(letters):
    print(letter)
# (0, 'A')  # 可以看到通过循环提取出的内容是元组
# (1, 'b')
# (2, 'c')
# 。。。以此类推
# 我们输出的是letter，也就是说letter就是元组，进一步可以对其再进行解包
names = ["Tom", "Jerry", "Mickey"]
for name in enumerate(names):
    print(name[0], name[1])  #   直接取出元组中的索引和内容
# 0 Tom
# 1 Jerry
# 2 Mickey
# 实际上这样的解包操作在循环开始时就可以进行，下面的循环和上面的结果一致
for index, name in enumerate(names):
    print(index, name)  #   局部变量会直接被赋予值并输出出来

# 由于列表是有序的，又不是元组那样只读的，那么就可以通过一些方法给列表进行添加和删除
# 添加元素append()
names.append("Donald")  # 在列表末尾添加元素“Donald”
print(names)  # 输出["Tom", "Jerry", "Mickey", "Donald"]
# 添加元素insert()
names.insert(0, "Daisy")  # 在索引0的位置插入元素“Daisy”
print(names)  # 输出["Daisy", "Tom", "Jerry", "Mickey", "Donald"]
# 移除元素remove()
names.remove(
    "Daisy"
)  # 移除元素“Daisy”，元素一定是确定值的，如果有多个值，那就需要循环移除了
print(names)  # 输出["Tom", "Jerry", "Mickey", "Donald"]
# 删除元素pop()
names.pop(0)  # 删除索引为0的元素
print(names)  # 输出["Jerry", "Mickey", "Donald"]
# pop这个单词字面意思有推出的意思，所以如果不加索引，那么会直接删除最后一个元素
names.pop()  # 删除最后一个元素
print(names)  # 输出["Jerry", "Mickey"]
# 随便添加几个名字，保证列表足够操作
names.append("Tom")
names.append("Jerry")
names.append("Mickey")
# 使用del也可以删除列表中的元素，甚至可以清除一个区间索引的元素
print(names)  # 输出["Jerry", "Mickey", "Tom", "Jerry", "Mickey"]
del names[0]  # 删除索引为0的元素
del names[0:3]  # 删除索引为0到2的元素
print(names)  # 输出["Mickey"]，即列表只剩下最后一个元素
# 如果我们想要直接清空列表的话，使用clear函数即可
names.clear()

# Python其实自带了列表的查找函数，比如index函数，可以用来查找列表中的元素
# index函数会返回元素在列表中的索引，如果元素不在列表中，那么会报错
letters = ["a", "b", "c", "d", "e"]
print(letters.index("c"))  # 输出2

# 这种查找方式就需要你先确定某个值是否存在于列表中
a = "d"
if a in letters:
    print(letters.index(a))  # 输出3
else:
    print(f"{a} is not in letters")

# Python还自带了count函数，可以用来统计列表中某个元素出现的次数
letters = ["a", "b", "c", "d", "e", "a", "b", "c", "d", "e"]
print(letters.count("a"))  # 输出2
# count函数的效率并不高，因为它是遍历整个列表的，所以如果列表很大，那么效率会很低

# 结合index和count函数，你就可以实现同时查找到元素和元素出现的次数
if a in letters:
    print(
        f"{a}'s index is {letters.index(a)} and there are {letters.count(a)} {a} in the list"
    )
else:
    print(f"{a} is not in letters")

# 由于列表的内容是可以被改变的，那么当一个列表内容被多次修改后，我们自然想要对列表进行规整化处理
# Python提供了sort函数，可以用来对列表进行排序
numbers = [12, 23, 32, 14, 5, 26, 17, 48, 39, 10]
numbers.sort()  # 对列表进行排序
print(numbers)  # 输出[5, 10, 12, 14, 17, 23, 26, 32, 39, 48]
# sort函数默认是从小到大排序，如果想要从大到小排序，可以传入reverse参数
numbers.sort(reverse=True)
print(numbers)  # 输出[48, 39, 32, 26, 23, 17, 14, 12, 10, 5]
# sort函数会直接修改列表，因此不需要返回值，但是sort函数只能对数字进行排序
# 如果想要不修改列表，甚至对字符串进行排序，就需要使用sorted函数
letters = ["e", "a", "b", "d", "c"]
numbers = [12, 23, 32, 14, 5, 26, 17, 48, 39, 10]
letters = sorted(letters)  # 实际上这行代码没有任何效果
print(f"The sorted letters is {sorted(letters)}")
numbers = sorted(numbers)  # 实际上这行代码没有任何效果
print(f"The sorted numbers is {numbers}")
print(letters)  # 输出['a', 'b', 'c', 'd', 'e']
print(numbers)  # 输出[5, 10, 12, 14, 17, 23, 26, 32, 39, 48]
# sorted函数会返回一个新的列表，而不会修改原来的列表
# 和sort函数一样，你也可以使用reverse参数倒序排序
# sorted(可迭代对象Iterable, key=排序依据, reverse=是否倒序)
print(
    f"The sorted letters is {sorted(letters, reverse=True)}"
)  # 输出['e', 'd', 'c', 'b', 'a']

# 对于简单的内容我们可以使用sorted函数，但是对于复杂的内容，比如字典或元组，就需要使用sorted函数的key参数了
items = [("Banana", 20), ("Apple", 30), ("Orange", 10), ("Pear", 15)]
items.sort()  # 这样操作并不会报错，但是实际上不会改变任何数据
print(items)  # 输出[('Apple', 30), ('Banana', 20), ('Orange', 10), ('Pear', 15)]
# 你可能听说过lambda函数，它是一种匿名函数，可以用来代替函数名
# 可以将其理解为一种一行就能写完的迷你小函数
# 它的语法是 lambda 参数: 返回值(lambda parameters:expression)
items = sorted(items, key=lambda item: item[1])  # 按照元组中的第二个元素进行排序
print(items)  # 输出[('Orange', 10), ('Pear', 15), ('Banana', 20), ('Apple', 30)]
# 上面的lambda函数和这样定义的简单函数类似，lambda后直接跟 参数:返回值，就是一个小函数
# def sort_item(item):
#     return item[1]

# 同样的，如果想要倒序排序，可以传入reverse参数
items = [("Banana", 20), ("Apple", 30), ("Orange", 10), ("Pear", 15)]
sorted(items, key=lambda item: item[1], reverse=True)  # 按照第二个值倒序
print(items)  # 输出[('Banana', 20), ('Apple', 30), ('Orange', 10), ('Pear', 15)]

# 当我们想要将列表中的元组内的数字提取出来形成新的数字列表时，就可以使用map函数了
items = [("Product1", 20), ("Product2", 30), ("Product3", 10), ("Product4", 15)]

# 传统的做法是通过循环去赋值
prices = []
for item in items:
    prices.append(item[1])
print(prices)  # 输出[20, 30, 10, 15]

# 实际上使用map函数可以更加简洁地实现相同的功能
# map函数会对传入的可迭代对象(参数2)的每一项执行传入的函数(参数1)，并最终返回一个迭代器对象
prices = []
prices = map(lambda item: item[1], items)
print(prices)  # 这样会输出map object的地址
# 将map对象转换为list对象即可看到其中的内容
print(list(map(lambda item: item[1], items)))  # 输出[20, 30, 10, 15]

# 当我们想要快速筛选时，可以使用filter函数
# filter函数会对传入的可迭代对象(参数2)的每一项执行传入的函数(参数1)，并最终返回一个迭代器对象
# 同map函数不同的是，filter函数要求传入的函数(参数1)必须返回布尔值，只有返回True时才被保留
# 该函数会返回满足条件的项
items = [("Product1", 20), ("Product2", 30), ("Product3", 10), ("Product4", 15)]
filtered = filter(lambda item: item[1] >= 20, items)
print(filtered)  # 输出filter object的地址
print(list(filtered))  # 输出[('Product1', 20), ('Product2', 30)]

# 你可能注意到只有使用list()和tuple()等函数才能将map和filter函数的结果输出出来
# 实际上list()和tuple()等函数会将传入的参数转换为列表或元组
# 这是因为为了节省内存，map和filter不会立刻生成结果，而是生成一个迭代器
# 只有在迭代的时候才会进行计算，而list()和tuple()正好就是触发迭代的方式
# 实际上map和filter的返回值迭代器只允许遍历一次，通过下面的例子可以看出
new_items = [("item1", 10), ("item2", 20), ("item3", 30)]
filtered_items = filter(lambda item: item[1] >= 20, new_items)
print(list(filtered_items))  # 输出[('item2', 20), ('item3', 30)]
print(list(filtered_items))  # 输出空列表
# 更深入一点，list函数和tuple函数实际上做了类似于list comprehension(列表推倒式)的处理
# 列表推倒式被称为Python里最优雅、最快、最常用的 “一键造列表” 语法
# 如果可以使用列表推倒式的话，90%的情况下尽量使用列表推倒式，而不是map+list或filter+tuple的形式
items = [("Product1", 20), ("Product2", 30), ("Product3", 10), ("Product4", 15)]
prices = [item[1] for item in items]  # 循环提取items中每个item的item[1]，并生成新的列表
# prices = [item[1] for item in items if item[1] >= 20] # 添加过滤条件，只提取大于等于20的item[1]
print(prices)  # 输出[20, 30, 10, 15]
# 可以看到直接使用列表推倒式，代码不再有因为调用函数而产生的更多括号，逗号，整个语句更加清晰、更简洁、更易读、更高效

# 之前的例子中我们在filter函数中使用了lambda函数进行过滤，同样我们也可以使用列表推倒式来代替filter函数
filtered = [item for item in items if item[1] >= 20]
print(filtered)  # 输出[('Product1', 20), ('Product2', 30)]
# 列表推倒式中，第一个item代表后面的for item in items中提取的item是什么，然后才是筛选的语句
# 即如果提取出的item，它的item[1]>=20，才会被保留，如此便实现了过滤功能

# 有拆分列表就有合并列表，如果我们想把两个列表合并成一个列表，可以使用zip函数
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# 同样，为了输出这个列表而不是输出zip对象地址，还需要使用list函数
combined = list(zip(list1, list2))
print(combined)  # 输出[(1, 4), (2, 5), (3, 6)]
# zip函数会把两个列表中的元素按照索引位置一一对应，然后合并成一个元组列表
# 如果两个列表的长度不同，zip函数会以较短的列表为准进行合并
# 事实上zip函数可以接收多个可迭代对象，由于字符串实际上也是一种可迭代对象，所以我们会有这样的例子
letter1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
letter2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(zip(letter1, letter2, number1)))
# 和其他语言需要手动遍历数组不同，python的zip函数可以自动完成这个过程
# 你只需要一行代码，就可以实现其他语言需要多行才能完成的遍历过程
