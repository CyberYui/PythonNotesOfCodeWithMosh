# ==============================================
# 第1章 字符串常用操作
# 核心：字符串是不可变类型，所有方法都返回新字符串
# ==============================================
sample_str = "    Hello, World!    "

# 基础查询
print("原字符串:", sample_str)
print("查找'World'的索引:", sample_str.find("World"))
print("变量类型:", type(sample_str))

# 常用格式化/清理方法
print("首字母大写:", sample_str.capitalize())
print("去除两端空格:", sample_str.strip())

# 索引与切片
text_str = "CyberIsPracticingProgrammingBasicLanguage"
print("第一个字符:", text_str[0])
print("最后一个字符:", text_str[-1])
print("切片 0~5, 左闭右开:", text_str[0:5])
print("从2到11, 左闭右开:", text_str[2:11])
print("取全部:", text_str[0:])

# 大小写转换
upper_str = text_str.upper()
print("转大写:", upper_str)
print("原字符串不变:", text_str)

# 字符串拼接与替换
str1 = "Hello"
str2 = "World"
print("拼接:", str1 + " " + str2)
print(f"f-string格式化: {str1} {str2}")
print(f"f-string表达式: {len(str1)} {2+2}")

# replace 生成新字符串
replaced_str = str1.replace("l", "k")
print("替换后:", replaced_str)
print("原字符串不变:", str1)

# ==============================================
# 第2章 数字类型与运算
# 核心：整数、浮点数、复数、数学运算、math模块
# ==============================================
int_num = 10
float_num = 1.1
print("int类型:", type(int_num))
print("float类型:", type(float_num))

# 复数
complex_num = 10 + 1j
print("复数:", complex_num)
print("实部:", complex_num.real)
print("虚部:", complex_num.imag)
print("复数类型:", type(complex_num))

# 基础运算
print("地板除 10//3, 只保留整数部分:", 10 // 3)
print("取模 10%3, 只保留余数:", 10 % 3)
print("幂运算 2**3, 2的3次方:", 2**3)

# 常用数学函数
print("四舍五入 round(2.6):", round(2.6))
# 如果是2.5四舍五入结果会是2
# 因为Python的round函数采用的是银行家舍入法（Banker's Rounding）当遇到.5时会向最近的偶数舍入
print("保留1位 round(2.55,1):", round(2.55, 1))
print("绝对值 abs(-5):", abs(-5))

# math 模块
import math

print("平方根 sqrt(16):", math.sqrt(16))
print("向上取整 ceil(2.3):", math.ceil(2.3))
print("向下取整 floor(2.7):", math.floor(2.7))

# ==============================================
# 第3章 布尔值与真假判断
# 核心：空值、0、空容器 都是 False，其他为 True
# ==============================================
print("空集合 bool(set()) →", bool(set()))
print("空字典 bool({}) →", bool({}))
print("空列表 bool([]) →", bool([]))
print("空元组 bool(()) →", bool(()))
print("空字符串 bool('') →", bool(""))
print("0 bool(0) →", bool(0))
print("0.0 bool(0.0) →", bool(0.0))
print("None →", bool(None))
print("False →", bool(False))
print("True →", bool(True))

# 三元表达式
age = 10
print("左真右假: Truthy" if age >= 10 else "Falsy")

# 进制
bin_num = 0b10
print("二进制 0b10 →", bin_num)
hex_num = 0x12C
print("十六进制 0x12C →", hex_num)
print("二进制+十六进制结果:", bin_num + hex_num)

# ==============================================
# 第4章 流程控制：if / while / for
# 核心：控制程序执行顺序，是所有逻辑的基础
# ==============================================
# if 判断
if age >= 10:
    print("年龄大于等于10")
elif age >= 5:
    print("年龄大于等于5但是小于10")
else:
    print("年龄小于5")

# while 循环
a, b = 1, 5
while a < b:
    print(f"当前 a = {a}")
    a += 1
    if a == 3:
        print("a=3，退出循环")
        break

# 变量交换（Python特色）
a, b = b, a
print(f"交换后 a={a}, b={b}")

# ==============================================
# 第5章 列表 list
# 核心：有序、可变、可重复，最常用容器
# ==============================================
list1 = [1, 2, 3]
list2 = ["a"] * 3
str_list = list("Hello")
combined_list = list1 + list2 + str_list

print("合并列表:", combined_list)
print("列表反转:", combined_list[::-1])

# 解包
# *other 是一个特殊的语法，表示将剩余的元素放在一个叫other的列表中
first, second, third, *other = combined_list
print(
    "解包前3个+剩余:",
    "first=",
    first,
    "second=",
    second,
    "third=",
    third,
    "other=",
    other,
)

first, *other, third, last = combined_list
print(
    "头尾+中间剩余:", "first=", first, "other=", other, "third=", third, "last=", last
)

# 增删改查
test_list = []
# append是在列表末尾添加一个元素
test_list.append(1)
test_list.append(2)
test_list.append(3)
# insert是在指定索引位置插入一个元素
test_list.insert(0, "a")
test_list.insert(2, "b")
print("增/插后:", test_list)

# pop是根据索引删除元素，默认删除最后一个元素
test_list.pop(-1)
# remove是根据值删除元素，如果有重复值只会删除第一个匹配到的元素
test_list.remove("a")
print("删后:", test_list)

# 索引删除
num_list = [1, 2, 3, 4, 5, "a", "b", "c", 0, "k"]
print("'k'的索引:", num_list.index("k"))
# del是根据索引删除元素，和pop不同的是del不会返回被删除的元素
del num_list[9]
print("del删除后:", num_list)

# 排序
numbers1 = [48, 39, 32, 14, 5]
# 原地排序, 直接改变原列表
numbers1.sort()
print("原地升序:", numbers1)
# 原地降序, reverse=True参数会让sort方法按照降序排序
numbers1.sort(reverse=True)
print("原地降序:", numbers1)

numbers2 = [7, 3, 5, 6]
# sorted函数会返回一个新的列表，原列表不变
sorted_num = sorted(numbers2, reverse=True)
print("新列表sorted_num是原列表降序:", sorted_num)
print("原列表numbers2不变:", numbers2)

# ==============================================
# 第6章 lambda / zip / enumerate / map
# 核心：简化代码、快速组合/遍历数据
# ==============================================
# lambda 简易函数
double = lambda x: x * 2  # 一行代码定义一个函数，参数是x，返回值是x的两倍
print("lambda 计算 1*2:", double(1))

# zip 打包
num_zip = [5, 4, 3, 2, 1]
char_zip = ["a", "b", "c", "d", "e"]
# 将两个列表按照索引位置一一对应打包成一个元组
zip_result = tuple(zip(num_zip, char_zip))
print("zip打包:", zip_result)
# 将元组转换为字典
zip_dict = dict(zip_result)
print("zip转字典:", zip_dict)

# 排序+字典推导
sorted_zip = sorted(zip_result, key=lambda x: x[0])
dict_from_zip = {k: v for k, v in sorted_zip}
print("排序后字典:", dict_from_zip)

# enumerate 索引+值
enum_list = [10, 20, 30]
enum_dict = {}
for idx, val in enumerate(enum_list):
    enum_dict[idx] = val
print("enumerate转字典:", enum_dict)

# map 映射
name_list = ["Tom", "Jerry"]
name_len = list(map(len, name_list))
print("map计算长度:", name_len)

# ==============================================
# 第7章 字典 dict
# 核心：键值对，查找极快，无序（3.7+有序）
# ==============================================
# 两种创建方式
user_dict1 = {"Tom": 10, "Jerry": 8}
user_dict2 = dict(Mickey=12, Donald=9)

# 合并
user_dict1.update(user_dict2)
print("合并字典:", user_dict1)

# 增/查
user_dict1["Jacky"] = 15
print("Jacky的成绩:", user_dict1["Jacky"])
print("Jacky的成绩（get）:", user_dict1.get("Jacky"))

# 键/值/项
print("所有键:", list(user_dict1.keys()))
print("所有值:", list(user_dict1.values()))
print("所有键值对:", list(user_dict1.items()))

# 按值排序
sorted_dict = dict(sorted(user_dict1.items(), key=lambda x: x[1], reverse=True))
print("按值降序:", sorted_dict)

# 清空
user_dict2.clear()

# ==============================================
# 第8章 推导式（列表/字典）
# 核心：极简创建容器，Python 最优雅语法之一
# ==============================================
# 列表推导式
even_list = [i for i in range(20) if i % 2 == 0]
print("偶数列表:", even_list)

# 字典推导式
square_dict = {i: i**2 for i in range(20) if i % 2 == 0}
print("偶数平方字典:", square_dict)

# ==============================================
# 第9章 数组 array（了解）
# ==============================================
from array import array

int_array = array("i", [1, 2, 3, 4, 5])
print("数组类型:", type(int_array))
print("数组内容:", int_array)

# ==============================================
# 第10章 集合 set
# 核心：无序、不重复，用于去重/交并差
# ==============================================
set1 = set([5, 3, 2, 4, 1])
set2 = {i for i in range(20) if i % 2 == 0}

print("并集 |:", set1 | set2)
print("交集 &:", set1 & set2)
print("差集 -:", set1 - set2)
print("对称差集 ^:", set1 ^ set2)

# ==============================================
# ================= 核心总结 ==================
# ==============================================
"""
📌 最重要知识点 + 记忆方法（必看）
1. 字符串
不可变：所有方法都返回新字符串
常用：strip() upper() replace() find()
记忆：字符串不改自己，只生儿子
2. 数字运算
// 地板除
% 取模
** 幂
记忆：斜杠是除，双斜杠向下取整
3. 真假判断
空容器、0、None、空串 → 全是 False
记忆：空 = 假，非空 = 真
4. 列表
有序、可变、可重复
增：append insert
删：pop remove del
记忆：列表万能，存啥都行
5. 字典
键唯一、查找快
创建：{k:v} 或 dict(k=v)
记忆：字典查得最快，键不能重复
6. 推导式
一行生成列表 / 字典
记忆：要简洁，用推导式
7. 集合
去重、交并差
记忆：集合天生去重
8. lambda / zip / map
简化代码
记忆：简单函数用 lambda，打包用 zip，映射用 map
"""
