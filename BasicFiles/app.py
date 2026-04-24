mystr = "    Hello, World!    "
print("mystr:", mystr)  # 输出原字符串，包含两端的空格
print("mystr.find('World'):", mystr.find("World"))  # 输出 "World" 在字符串中的索引
print("type(mystr):", type(mystr))  # 输出字符串的类型
newstr = mystr.format()  # 字符串的 format 方法，返回一个新的字符串
print("newstr:", newstr)  # 输出使用 format 方法返回的新字符串
print(
    "mystr == newstr:", mystr == newstr
)  # 输出比较结果，说明 mystr 和 newstr 是相同的字符串对象

print(mystr.capitalize())  # 将字符串的第一个字符转换为大写，其他字符转换为小写
print(mystr.strip())  # 删除字符串两端的空格

mystr = "CyberIsPracticingProgrammingBasicLanguage"
print(mystr[0])
print(mystr[-1])
print(mystr[0:5])
print(mystr[0:])  # same as mystr
print(mystr[2:11])

newstr = mystr.upper()  # 将字符串转换为大写
print(newstr)  # 输出转换后的字符串
print(mystr)  # 输出原字符串，说明原字符串是不变的

mystr = "Hello"
newstr = "World"
print(mystr + " " + newstr)  # 输出连接后的字符串
print(f"{mystr} {newstr}")  # 使用 f-string 格式化字符串
print(f"{len(mystr)} {2 + 2}")  # 在 f-string 中使用表达式
print(mystr.replace("l", "k"))
print(mystr)  # 输出原字符串，说明原字符串是不变的

x = 10
y = 20
z = 1.1
print(type(x))  # 输出 x 的类型
print(type(z))  # 输出 z 的类型
m = x + 1j
print(m)  # 输出 m 的值
print(m.real)  # 输出 m 的实部
print(m.imag)  # 输出 m 的虚部
print(type(m))  # 输出 m 的类型
print(10 // 3)  # 输出整数的地板除结果，结果是一个整数
print(10 % 3)  # 输出整数的模运算结果，结果是一个整数
print(2**3)

round(2.5)  # 输出 2.5 四舍五入后的结果，结果是一个整数
print(round(2.5))  # 输出 2.5 四舍五入后的结果，结果是一个整数
print(round(2.55, 1))  # 输出 2.55 四舍五入到小数点后一位的结果，结果是一个浮点数
print(abs(-5))  # 输出 -5 的绝对值，结果是一个整数

import math  # 导入 math 模块，提供数学函数和常量

print(math.sqrt(16))  # 输出 16 的平方根，结果是一个浮点数
print(math.ceil(2.3))  # 输出 2.3 向上取整后的结果，结果是一个整数
print(math.floor(2.7))  # 输出 2.7 向下取整后的结果，结果是一个整数

print(bool(set()))  # 输出一个空集合的布尔值，结果是 False
print(bool({}))  # 输出一个空字典的布尔值，结果是 False
print(bool([]))  # 输出一个空列表的布尔值，结果是 False
print(bool(()))  # 输出一个空元组的布尔值，结果是 False
print(bool(""))  # 输出一个空字符串的布尔值，结果是 False
print(bool(0))  # 输出整数 0 的布尔值，结果是 False
print(bool(0.0))  # 输出浮点数 0.0 的布尔值，结果是 False
print(bool(None))  # 输出 None 的布尔值，结果是 False
print(bool(False))  # 输出 False 的布尔值，结果是 False
print(bool(True))  # 输出 True 的布尔值，结果是 True
print(bool(1))  # 输出整数 1 的布尔值，结果是 True

age = 10  # 获取用户输入的年龄，返回一个字符串
print("Falsy values" if int(age) >= 10 else "Truthy values")

x = 0b10
x = 0x12C
y = 0b10 + 0x12C
print(y)

if age >= 5:
    print(f"Age is more than or equal to 5")
elif age >= 10:
    print(f"Age is more than or equal to 10")
else:
    print(f"Age is less than 5")

# for x in "Helloworld":
#     print(x)

# for i in range(0, 5):
#     print(i)

# for i in range(0, 50, 2):
#     if i == 0:
#         continue
#     print(i)

animals = [
    "cat",
    "dog",
    "rabbit",
    "hamster",
    "parrot",
    "fish",
    "turtle",
    "snake",
    "lizard",
    "frog",
]
# for animal in animals:
#     if animal.startswith("s"):
#         print(f"Found {animal}!")
#         break
# else:
#     print("Not Found!")

a = 1
b = 5
while a < b:
    print(f"Now a is: {a}")
    a += 1
    if a == 3:
        print("a is now 3, breaking the loop")
        break

a, b = b, a
print(f"Now a is: {a}, and b is: {b}")

firstlist = [1, 2, 3]
secondlist = ["a"] * 3
thirdlist = "Hello"
wholelist = firstlist + secondlist + list(thirdlist)
print(wholelist)  # 输出连接后的列表
# for i in wholelist:
#     print(i)
print(wholelist[::-1])
first, second, third, *other = wholelist
print(first)  # 输出列表的第一个元素
print(second)  # 输出列表的第二个元素
print(third)  # 输出列表的第三个元素
print(other)  # 输出列表中剩余的元素，结果是一个列表
print(wholelist)
first, *other, third, last = wholelist
print(first)  # 输出列表的第一个元素
print(other)  # 输出列表中剩余的元素，结果是一个列表
print(third)  # 输出列表的倒数第二个元素
print(last)  # 输出列表的最后一个元素

firstenumerate = enumerate(wholelist)
newdict = {}
for index, truevalue in firstenumerate:
    newdict[index] = truevalue

print(newdict)  # 输出一个字典，键是列表元素的索引，值是列表元素的值

wholelist = []
wholelist.append(1)
wholelist.append(2)
wholelist.append(3)
print(wholelist)  # 输出添加元素后的列表
wholelist.insert(0, "a")
wholelist.insert(2, "b")
wholelist.insert(5, "c")
print(wholelist)  # 输出插入元素后的列表
wholelist.pop()
print(wholelist)  # 输出删除元素后的列表
wholelist.remove("a")
wholelist.remove(2)
print(wholelist)  # 输出移除元素后的列表

wholelist = [1, 2, 3, 4, 5, "a", "b", "c", 0, "k"]
print(wholelist.index("k"))
del wholelist[9]
print(wholelist)  # 输出删除元素后的列表
