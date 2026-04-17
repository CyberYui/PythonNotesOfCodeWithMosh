"""这个文件中会展示局部变量和全局变量"""
# python中没有块级作用域，只有函数级作用域和全局作用域


# 下面这个例子中，message是一个局部变量，尽管它是在函数的if语句块中定义的，但它在整个函数中都是可调用的
def greet(a: int):
    if a > 0:
        message = "Nice!"
    print(message)
    return a


greet(1)  # 输出: Nice!


# 下面这个例子中，message是一个全局变量，在函数greet中也可以访问到
message = "Hello, World!"


def greet(a: int):
    if a > 0:
        print(message)
    return a


greet(1)  # 输出: Hello, World!


# 事实上尽管是全局变量，但在函数中我们也可以修改它的值
message = "Hello, World!"


def greet(a: int):
    # 避免使用global陈述，因为它会使代码更难理解和维护
    global message  # 声明使用全局变量
    if a > 0:
        message = "Not really Nice!"
    print(message)
    return a


greet(1)  # 输出: Not really Nice!
print(message)  # 输出: Not really Nice!
