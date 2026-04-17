"""这是一个简单的Python程序，用于演示 Python 基础语法"""
import math  # 导入 math 模块，提供数学函数和常量

print("Hello World 🐱")
print("*" * 10)
print("Hello World")

course = "Python Programming"
print(course)       # 输出字符串
print(len(course))  # 输出字符串的长度
print(course[0])    # 输出字符串的第一个字符
print(course[-1])   # 输出字符串的最后一个字符
print(course[0:3])  # 输出字符串的前三个字符,结束索引不包含在内
print(course[0:])   # 输出字符串的所有字符
print(course[:5])   # 输出字符串的前五个字符
print(course[:])    # 输出字符串的所有字符

# \" 转义字符，表示一个双引号
# \' 转义字符，表示一个单引号
# \\ 转义字符，表示一个反斜杠
# \n 转义字符，表示一个换行符
# \t 转义字符，表示一个制表符吗，实际上就是个空格
course = "Python \nProgramming"

print("*" * 10)

# pylint: disable=invalid-name  # 忽略当前文件的命名风格检查
first = "Yui"
last = "Cyber"
full = first + " " + last
full = f"{first} {last}"  # 使用 f-string 格式化字符串
full = f"{len(first)} {2 + 2}"  # 在 f-string 中使用表达式
print(full)  # 输出连接后的字符串

print("*" * 10)

# Everything in Python is an object, including strings. This means we can call methods on strings.
course = "Python Programming"
course.upper()  # 将字符串转换为大写
print(course.upper())  # 输出转换后的字符串
print(course)  # 输出原字符串，说明字符串是不可变的
course_capital = course.capitalize()  # 将字符串的第一个字符转换为大写，其他字符转换为小写
print(course_capital)  # 输出转换后的字符串
print(course)  # 输出原字符串，说明字符串是不可变的

course.lower()  # 将字符串转换为小写
print(course.lower())  # 输出转换后的字符串
print(course.title())  # 将字符串的每个单词的首字母转换为大写

print("*" * 10)
course = "   Python Programming   "
print(course)  # 输出原字符串，包含两端的空格
print(course.strip())  # 去除字符串两端的空格
print(course.lstrip())  # 去除字符串左侧的空格
print(course.rstrip())  # 去除字符串右侧的空格

print(course.find("pro"))  # 查找字符串中第一个 "pro" 的索引
print(course.find("Pro"))  # 查找字符串中第一个 "Pro" 的索引，区分大小写
print(course.replace("P", "J"))  # 将字符串中的 "P" 替换为 "J"
print("Pro" in course)  # 检查字符串中是否包含 "Pro"
# Find方法返回子字符串在字符串中第一次出现的位置索引，如果没有找到则返回 -1
# 而 in 操作符返回一个布尔值，表示子字符串是否存在于字符串中

print("swift" not in course)  # 检查字符串中是否不包含 "swift"

print("*" * 10)

x = 10  # 这是一个整数对象
x = 1.1  # 这是一个浮点数对象
x = 1 + 2j  # 这是一个复数对象
print(type(x))  # 输出变量 x 的类型
print(10 + 3)  # 输出整数的加法结果
print(10 - 3)  # 输出整数的减法结果
print(10 * 3)  # 输出整数的乘法结果
print(10 / 3)  # 输出整数的除法结果，结果是一个浮点数
print(10 // 3)  # 输出整数的地板除结果，结果是一个整数
print(10 % 3)  # 输出整数的模运算结果，结果是一个整数
print(10 ** 3)  # 输出整数的幂运算结果，结果是一个整数

x = 10
x += 3  # 等价于 x = x + 3
print(x)  # 输出 x 的值
x -= 3  # 等价于 x = x - 3
print(x)  # 输出 x 的值
x *= 3  # 等价于 x = x * 3
print(x)  # 输出 x 的值
x /= 3  # 等价于 x = x / 3
print(x)  # 输出 x 的值

print("*" * 10)
round(2.9)  # 将 2.9 四舍五入到最接近的整数
print(round(2.9))  # 输出 3
print(abs(-2.9))  # 输出 -2.9 的绝对值

math.ceil(2.9)  # 将 2.9 向上取整到最接近的整数
print(math.ceil(2.9))  # 输出 3
math.floor(2.9)  # 将 2.9 向下取整到最接近的整数
print(math.floor(2.9))  # 输出 2
math.sqrt(16)  # 计算 16 的平方根
print(math.sqrt(16))  # 输出 4.0

print("*" * 10)
# input() 函数用于从用户输入获取数据，返回一个字符串
# name = input("What is your name? ")  # 提示用户输入名字
# print(f"Hi {name}!")  # 输出问候语，使用 f-string 格式化字符串
# print("*" * 10)

# 练习：计算圆的面积
# radius = input("请输入圆的半径: ")  # 获取用户输入的半径，返回一个字符串
# radius = float(radius)  # 将字符串转换为浮点数
# area = math.pi * radius ** 2  # 计算圆的面积，使用 math.pi 常量和幂运算符
# print(f"圆的面积是: {area:.2f}")  # 输出圆的面积，保留两位小数
# print("*" * 10)

# Falsy 值：False, None, 0, 0.0, 0j, '', [], (), {}, set()
# Truthy 值：除了 Falsy 值以外的所有值都是 Truthy 值
print(bool(""))  # 输出 False，因为空字符串是 Falsy 值
print(bool("False"))  # 输出 True，因为非空字符串是 Truthy 值
print(bool(0))  # 输出 False，因为 0 是 Falsy 值
print(bool(0.0))  # 输出 False，因为 0.0 是 Falsy值
print(bool(1))  # 输出 True，因为 1 是 Truthy 值
print(bool([]))  # 输出 False，因为空列表是 Falsy 值
print(bool([1, 2, 3]))  # 输出 True，因为非空列表是 Truthy 值
print(bool(None))  # 输出 False，因为 None 是 Falsy 值
print(bool(False))  # 输出 False，因为 False 是 Falsy 值
print(bool(True))  # 输出 True，因为 True 是 Truthy 值

# Python中的三元运算符
age = 20
# 根据条件表达式的结果选择 "Eligible" 或 "Not Eligible"
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)  # 输出 "Eligible" 因为 age 大于等于 18

# 同逻辑的 if-else 语句
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)  # 输出 "Eligible" 因为 age 大于等于 18
