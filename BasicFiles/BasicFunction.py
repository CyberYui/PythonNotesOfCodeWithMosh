"""这部分用来进行Function(函数)的练习"""
# 一个函数通过def关键字来定义，后面跟着函数的名字和括号，括号里可以有参数

# pass是一个占位符，表示这个函数还没有实现
# def increment(number, by):
#     pass


def increment(number, by):
    return number + by


# python的函数实际上可以返回多个值，返回值用逗号分隔开来
def number_source(number, by):
    return (number, number+by)


def increment_and_decrement(number, by):
    return number + by, number - by


# 这种直接输入参数值的调用称为位置参数，即按函数的位置传参
print(increment(2, 3))  # (2, 5)
# 返回的（2, 5）我们称为一个tuple（元组），它是一个不可变的序列，可以用来存储多个值
# 元组和列表的区别在于，元组是不可变的，而列表是可变的。元组用圆括号表示，列表用方括号表示
# 比如下面这两个number变量，一个是列表，一个是元组，列表可以修改，而元组不可以修改
number = [1, 2, 3]  # 这个number是一个列表，可以修改
number = (1, 2, 3)  # 这个number是一个元组，不可以修改
# 在输入参数的时候，我们可以使用关键字参数，这样就不需要按照位置来传递参数了
# 下面这三个调用都是一样的，都是传递了number=2和by=3这两个参数，只不过顺序不同而已
print(increment_and_decrement(2, by=3))
# 这种添加了参数名的关键字参数可以更清晰地表达参数的含义
print(increment_and_decrement(number=2, by=3))
print(increment_and_decrement(by=3, number=2))


# 如果在定义函数的时候，给参数指定了默认值，那么在调用函数的时候，如果没有传递这个参数，就会使用默认值
def new_increment(number, by=1):
    return number + by


print(new_increment(2))  # 这里没有传递by参数，所以使用默认值1，结果是3
print(new_increment(2, 3))  # 这里传递了by参数，所以使用传递的值3，结果是5


# 在定义函数时，我们一般会对参数进行类型注解，这样可以提高代码的可读性和可维护性，
# 虽然Python是一种动态类型语言，但类型注解可以帮助我们更好地理解函数的输入和输出
# docstring是一个字符串，放在函数的第一行，用来说明函数的功能和参数的含义
# 在定义函数时还需要指定返回值的类型，并对函数进行一段注释，说明函数的功能和参数的含义
# 比如通过-和>形成的→箭头就是用来指定返回值的类型的
def annotated_increment(num: int, by: int) -> tuple[int, int]:
    """这个函数用来对一个数字进行增量和减量的操作
参数：
    num (int): 要进行操作的数字
    by (int): 增量或减量
返回值：
    tuple[int, int]: 包含原始数字和增量后数字的元组
    """
    return (num + by, num - by)


# 我们一般在创建函数的时候会想要能传入任何类型的参数，来让函数更通用一些
# 我们可以使用Python的动态类型特性来实现这一点
# *numbers参数允许我们传入任意数量的位置参数，这些参数会被收集到一个元组中
# 函数会在其内部对这个元组进行操作来实现我们想要的功能，比如在这个例子中，我们想要计算所有传入数字的乘积
def multiply(*numbers):
    """这个函数接受任意数量的数字参数，并返回它们的乘积。"""
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3))  # 输出: 6
print(multiply(2, 3, 4))  # 输出: 24


# **kwargs参数允许我们传入任意数量的关键字参数，这些参数会被收集到一个字典中
def save_user(**user):
    """这个函数接受任意数量的关键字参数，并将它们作为用户信息保存。"""
    print("Saving user:")
    for key, value in user.items():
        print(f"{key}: {value}")
    return user


print(type(save_user))  # 输出: <class 'function'>

user1 = save_user(name="Alice", age=30, email="alice@example.com")
# 输出:
# Saving user:
# name: Alice
# age: 30
# email: alice@example.com
print(type(user1))  # 输出: <class 'dict'>
print(user1)  # 输出: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}

# 同其他程序语言的先声明后使用不同，Python的函数中无论在何处声明的变量，都可以在函数的任何地方使用
# 这是因为Python的函数是动态作用域的，即函数中的变量在函数内部都是可见的
# 也就是说Python没有块级作用域，只有函数作用域
def greet(a:bool):
    """这个函数仅作为展示，即使是在if语句中声明的变量，在整个函数中都是可以使用的"""
    # 在函数中定义全局变量同名变量是可行的, 但是函数中这样定义的变量实际上只是个局部变量，只是碰巧和全局变量重名了
    # 所以在函数中定义的变量不是修改全局变量的值，它是个局部变量，不影响全局变量本身的值
    message = "b"
    if a == True:
        name = "Alice"
    else:
        name = "Bob"
    print(f"Hello, {name}, {message}!")


# 当一个函数被声明到函数外部时，它就是一个全局变量
message = "a"
def greetagain():
    """这个函数用来修改并打印一个全局变量"""
    # Python中可以使用global关键字在函数中真正修改全局变量
    global message  # 声明使用的是全局变量message，这种做法是不被建议的
    message = "c"   # 此时修改的是全局变量
    print(message)


greet(True)
greetagain()    # 输出：c（全局变量被修改）
