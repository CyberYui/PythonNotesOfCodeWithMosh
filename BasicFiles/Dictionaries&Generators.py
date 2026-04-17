from sys import getsizeof

# 字典实际上就是一个键值对的集合，键必须是唯一的，值可以重复
# 一个很典型的例子就是PhoneBook，即电话簿，名字是唯一的，而电话号码可以重复
# 键一般是字符串，值可以是任意类型的对象
# 字典的定义方式有两种，一种是使用花括号{}，另一种是使用dict()函数
# 使用花括号定义字典
phone_book = {"Alice": "123-456-7890", "Bob": "987-654-3210", "Charlie": "555-555-5555"}
# 使用dict()函数定义字典
phone_book2 = dict(Alice="123-456-7890", Bob="987-654-3210", Charlie="555-555-5555")
# 访问字典中的值，可以使用键来访问
print(phone_book["Alice"])  # 输出: 123-456-7890
# 如果要向字典中添加新的键值对，可以直接赋值
phone_book["David"] = "111-222-3333"
print(
    phone_book
)  # 输出: {'Alice': '123-456-7890', 'Bob': '987-654-3210', 'Charlie': '555-555-5555', 'David': '111-222-3333'}
# 当我们想要输出一个不存在于字典中的键时，会抛出KeyError异常
# print(phone_book["Eve"])  # 这行代码会抛出KeyError异常，因为Eve这个键不存在于字典中
# 为了避免这种情况，我们可以使用get()方法来访问字典中的值，如果键不存在于字典中，get()方法会返回None或者我们指定的默认值
print(phone_book.get("Eve"))  # 输出: None
print(phone_book.get("Eve", "Not Found"))  # 输出: Not Found
# 删除字典中的键值对，可以使用del关键字
del phone_book["Bob"]
print(
    phone_book
)  # 输出: {'Alice': '123-456-7890', 'Charlie': '555-555-5555', 'David': '111-222-3333'}
# 当你想要遍历字典中的内容时，仅仅使用一个x可能不能得到想要的结果
for x in phone_book:
    print(x)  # 输出: Alice Charlie David
# 也就是说当你仅输出一个x时，你得到的是字典中的键，而不是值或者键值对
# 为了仅仅使用键就能得到每一个简直对，你需要这样做
# 需要注意的是，这里使用key而不是x，这只是一个习惯用法，你也可以使用其他变量名来代替key
for key in phone_book:
    print(
        key, phone_book[key]
    )  # 输出: Alice 123-456-7890 Charlie 555-555-5555 David 111-222-3333
# 针对此类循环，字典还提供了一些常用的方法，如keys()、values()和items()
print(phone_book.keys())  # 输出: dict_keys(['Alice', 'Charlie', 'David'])
print(
    phone_book.values()
)  # 输出: dict_values(['123-456-7890', '555-555-5555', '111-222-3333'])
print(
    phone_book.items()
)  # 输出: dict_items([('Alice', '123-456-7890'), ('Charlie', '555-555-5555'), ('David', '111-222-3333')])
# 借助items()方法，我们可以同时获取字典中的键和值，这样就不需要再通过键来访问值了
for key in phone_book.items():
    print(
        key
    )  # 输出: ('Alice', '123-456-7890') ('Charlie', '555-555-5555') ('David', '111-222-3333')
# 当然你也可以使用两个变量来同时获取键和值，实现对字典解包的效果
for x, y in phone_book.items():
    print(x, y)  # 输出: Alice 123-456-7890 Charlie 555-555-5555 David 111-222-3333

# 在之前我们可以通过循环创建列表
values = []
for x in range(5):
    values.append(x * 2)
# 这种循环会被我们使用List comprehension来替代，List comprehension是一种简洁的语法，可以让我们在一行代码中创建一个列表
values = [x * 2 for x in range(5)]
# 让我们深入一下这个语法
# [expression for item in iterable if condition]
# 在上面的values这个例子中，我们使用的是[expression for item in iterable]这种形式
# expression是指我们的循环内容，在例子中就是x * 2
# item是指我们循环中的变量，在这个例子中是x
# iterable是指我们要循环的对象，这个对象是可迭代的，在这个例子中是range(5)
# 当我们将中括号换成花括号时，我们就得到了一个集合
numbers = {x * 2 for x in range(5)}
print(numbers)  # 输出: {0, 2, 4, 6, 8}
# 集合中只有一个值，所以可以使用这种方式创建，那么对于有键值对的字典，我们一般会如何创建呢？
dictionary = {1: "x", 2: "y", 3: "z"}
print(dictionary)  # 输出: {1: 'x', 2: 'y', 3: 'z'}
# 可以看到每一个元素实际上就是 键:值 的形式，然后不同元素用逗号隔开了
# 如果使用循环我们可以这样创建一个字典
for x in range(5):
    dictionary[x] = x * 2
print(dictionary)  # 输出: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
# 因为能用循环创建字典，所以我们也可以使用Dictionary comprehension来创建字典
# 我们知道循环中的x是会叠加的，而由此我们便可以通过设置循环体来进行键值对的创建
dictionary = {x: x * 2 for x in range(5)}
print(dictionary)  # 输出: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# 由于有List comprehension，Set comprehension和Dictionary comprehension，我们自然会想到元组
tuple_comprehension = (x * 2 for x in range(5))
print(tuple_comprehension)  # 输出: <generator object <genexpr> at 0x104a5ea50>
# 可以看到我们得到的并不是一个元组，而是一个生成器对象
# 这是因为Python中没有真正意义上的Tuple comprehension
# 虽然我们可以使用圆括号来创建一个生成器对象，但它并不是真正意义上的Tuple comprehension
# 如果我们想要创建一个真正意义上的元组，就需要借助tuple()函数来将生成器对象转换成一个元组
tuple_comprehension = tuple(x * 2 for x in range(5))
print(tuple_comprehension)  # 输出: (0, 2, 4, 6, 8)

# 说到生成器，就不得不回到List开始说起
values = [x * 2 for x in range(5)]
# 这里通过一个列表推倒式创建了values，当我们针对大数据甚至是无限数时，使用列表就会遇到内存不足的问题
# 我们就会想有没有一种方法可以让我们在不占用大量内存的情况下创建一个可迭代的对象来生成这些值呢？
# 这时候我们就可以使用生成器表达式来创建一个生成器对象
# 生成器会在需要的时候才会生成下一个值，而不是一次性将所有的值都生成出来，这样就可以节省大量的内存
generator = (x * 2 for x in range(5))
print(generator)  # 输出: <generator object <genexpr> at 0x104a5ea50
# 我们可以使用类似的for循环来遍历list和generator的内容
for x in values:
    print(x)  # 输出: 0 2 4 6 8
for x in generator:
    print(x)  # 输出: 0 2 4 6 8
# 两者都输出了相同的结果，那么它们的区别在哪里呢？我们可以从sys模块引入getsizeof，并把元素增多来对比
values = [x * 2 for x in range(1000)]
generator = (x * 2 for x in range(1000))
print(getsizeof(values))  # 输出: 8856
print(getsizeof(generator))  # 输出: 112
# 可以看到当我们创建了一个包含1000个元素的列表时，它占用了8856字节的内存
# 而当我们创建了一个包含1000个元素的生成器时，它只占用了112字节的内存
# 这就是生成器的优势所在，它可以在不占用大量内存的情况下生成大量的值
# 尤其是当我们需要处理大数据或者无限数时，生成器是非常有用的工具

# 由于我们无法知道generator中有多少个元素，所以我们无法使用len()函数来获取生成器的长度
# print(len(generator))  # 这行代码会抛出TypeError异常，因为生成器对象没有长度
# 但是我们可以使用sum()函数来获取生成器中所有元素的和
print(sum(generator))  # 输出: 999000
# 需要注意的是，当我们使用sum()函数来获取生成器中所有元素的和时
# 生成器中的元素会被逐个生成出来并进行求和，直到生成器中的所有元素都被生成出来并求和完成后，生成器就会被耗尽
