"""这是一个简单的Python学习程序，包含了循环等基础知识点的练习"""
import random

for x in "Hi":
    print(x)
print("*" * 10)
for x in ['Mosh', 'John', 'Sara']:
    print(x)
print("*" * 10)
# 可以使用range()函数生成一个整数序列，常用于循环中
for x in range(3):
    print(x)
print("*" * 10)
# range(0，5) 生成一个整数序列，从 0 开始，到 5 结束，步长为 1
for x in range(0, 5):
    print(x)
print("*" * 10)
# range(5,10,2) 生成一个整数序列，从 5 开始，到 10 结束，步长为 2
# 步长为 2，表示每次增加 2，即输出 5、7、9
for x in range(5, 10, 2):
    print(x)
print("*" * 10)
# range返回的是一个可迭代对象，而不是一个列表。如果需要一个列表，可以使用 list() 函数将其转换为列表
# 多使用range的原因是它占用的内存更少，尤其是在生成大量整数时，
# 因为它不需要一次性将所有整数存储在内存中，而是按需生成整数。
print(range(5, 10, 2))  # 输出 range(5, 10, 2)
print(type(range(500000000000)))  # 输出 <class 'range'>
print(list(range(5, 10, 2)))  # 输出 [5, 7, 9]
print("*" * 20)
names = ['Mosh', 'John', 'Sara']
# name在循环中是一个临时变量，用于存储当前循环迭代到的元素值。
# 在每次循环迭代时，name会被赋值为列表names中的下一个元素，直到循环结束。
for name in names:
    # startswith() 方法用于检查字符串是否以指定的前缀开头，返回 True 或 False
    if name.startswith('M'):
        print("Found!")
        break  # 退出循环
else:
    print("Not Found!")  # 当循环正常结束时执行
print("*" * 20)
# 使用while循环来实现一个简单的猜数字游戏
guess = 0
answer = random.randint(0, 20)  # 生成一个 0 到 20 之间的随机数
while answer != guess:
    guess = int(input("Guess: "))  # 获取用户输入的猜测，并将其转换为整数
    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
print("You got it!")
print("*" * 20)
