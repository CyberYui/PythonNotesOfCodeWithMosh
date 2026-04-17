# 在Python中经常会遇到字符串转换为数字进行运算，或者将数字运算结果保存为字符串的情况
x = input("x: ")
# y = x + 1 # 这时会报错，因为input函数返回的是字符串类型，无法直接与整数进行运算
# 实际上如果是字符串相加，Python会进行拼接，比如 “1” + “1” = “11”
# 如果是数值相加，Python会进行数学运算，比如 1 + 1 = 2
# 这也是为什么Python会被称为强类型语言的原因
# 区别于JavaScript，JavaScript是弱类型语言，允许隐式转换，比如 “1” + 1 = “11”
# 为了解决不同类型相互计算报错的问题，我们需要使用类型转换函数
y = int(x) + 1 # 通过int函数将字符串转换为整数类型
print(y)
z = float(x) + 2.5 # 通过float函数将字符串转换为浮点数类型
print(z)
m = bool(x) # 通过bool函数将字符串转换为布尔类型，非空字符串转换为True，空字符串转换为False
print(m)
n = str(y) # 通过str函数将整数类型转换为字符串类型
print(n)

# 有一些默认为否的值称为Falsy，比如 "" 0 [] None (null)
# 这些值在被转换为布尔类型的时候，会被认为是“False”，其他的任何值都会是“True”
x = ""
print(bool(x)) # False
x = 0
print(bool(x)) # False
x = []
print(bool(x)) # False
x = None
print(bool(x)) # False
# x = (null) # Python中没有null，一般通过None来代替
x = "null" # 注意，这里的null是字符串，不是JavaScript中的null
print(bool(x)) # True
