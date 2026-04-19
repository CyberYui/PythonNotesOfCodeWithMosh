# Python Test Set 2 - Normal

**Time: 30 minutes**  
**Total Questions: 20**

---

## Question 1
What will be the output of this code?
```python
def multiply(a, b=2):
    return a * b

print(multiply(5))
print(multiply(5, 3))
```

A: The first print:10, first para is the value of a ,b will use default value 2, return 5*2=10;

The second print:15, a=5 & b=3,result is 15
**✅ 正确** - 解释正确，理解了默认参数的使用

## Question 2

Explain the difference between `append()` and `insert()` methods for lists.

A: append method will add an item in the bottom of list, insert method will insert to the top of list
**❌ 错误**
**你的答案：** append方法在列表末尾添加元素，insert方法在列表开头添加元素
**正确答案：** append()方法在列表末尾添加元素，insert(index, element)在指定位置插入元素
**解释：** insert()方法可以在任意指定位置插入元素，而不只是在开头

## Question 3
Write a function that takes a list of numbers and returns only the even numbers using list comprehension.

A: def even_in_list(list):

​	"""This function will return a list of even numbers of para list"""

​	even = []

​	for item in list:

​		if item//2:

​			even.insert(item)

​		else:

​			continue

​	return even
**❌ 错误**
**你的答案：**
```python
def even_in_list(list):
    """This function will return a list of even numbers of para list"""
    even = []
    for item in list:
        if item//2:
            even.insert(item)
        else:
            continue
    return even
```
**正确答案：**
```python
def get_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]
```
**错误原因：**
1. list是Python关键字，不应作为变量名
2. 偶数判断错误：item//2!=0不表示偶数，应该用x % 2 == 0
3. insert用法错误：insert(index, value)，不是insert(value)
4. 没有用到列表 comprehension

## Question 4

What is the purpose of the `global` keyword in Python? Provide an example.

A: global keyword is using in order to use a variable that was defined in a block, if you defined a variable in if block, but you want to use it outside the if block, you should use global signal to define it in if block.
**❌ 错误**
**你的答案：** global关键字用于在块中定义的变量，如果在if块中定义了一个变量，但想在块外使用，应该在if块中使用global信号定义它
**正确答案：** global关键字用于在函数内部修改全局变量，而不是在任何块中使用
**正确例子：**
```python
count = 0

def increment():
    global count  # 声明使用全局变量count
    count += 1
```
**解释：** global只能在函数内部使用，不能在if、while、for等块中使用。如果在函数内部修改全局变量，必须使用global关键字声明。

## Question 5
Write code to create a dictionary from two lists: `keys = ['a', 'b', 'c']` and `values = [1, 2, 3]`.

A: own_dict={}

for a,b in keys, values:

​	own_dict.add(keys,values)
**❌ 错误**
**你的答案：**
```python
own_dict={}
for a,b in keys, values:
    own_dict.add(keys,values)
```
**正确答案：**
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
own_dict = dict(zip(keys, values))
```
**解释：**
1. Python的for循环中，zip()用于同时遍历多个列表
2. 字典没有add方法，直接使用字典赋值
3. 正确的方法是使用zip()函数和dict()构造函数

## Question 6
Explain what lambda functions are and write a lambda function that squares a number.

A: The lambda function is a simple function inline of the code, instead of using def sentence to create.

Lambda a: a ** 2, a
**❌ 错误**
**你的答案：** lambda函数是代码内联的简单函数，不需要用def创建
**你的lambda语法：** Lambda a: a ** 2, a
**正确答案：**
```python
square = lambda a: a ** 2
```
**解释：** lambda语法是lambda 参数: 表达式，不是Lambda（大写），最后不需要逗号和a

## Question 7

What will be the output of this code?
```python
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))
```

A: [1,4,9,16,25]
**❌ 错误**
**你的答案：** [1,4,9,16,25]
**正确答案：** [2, 4, 6, 8, 10]
**解释：** map(lambda x: x * 2, [1, 2, 3, 4, 5])将每个元素乘以2，不是平方

## Question 8

Write a class `Person` with attributes `name` and `age`, and a method `greet()` that returns "Hello, my name is {name}".

A: class Person(self):

​	self.name = ""

​	self.age = 0



​	def greet(name):

​		return f"Hello, my name is {name}"
**❌ 错误**
**你的答案：**
```python
class Person(self):
    self.name = ""
    self.age = 0
    
    def greet(name):
        return f"Hello, my name is {name}"
```
**正确答案：**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name}"
```
**错误原因：**
1. 类定义不需要self参数
2. 属性应该在__init__方法中初始化
3. greet方法应该有self参数
4. 使用self.name访问实例属性

## Question 9
Explain inheritance in Python with a simple example of an Animal base class and a Dog derived class.

A: Since we have a class named Animal , it has a method like eat() , when we create a Dog class , with inheritance define, we don't need to create a new eat() method for Dog , we can still use this method when we create a dog object , like this condition, we call the Dog class is the inheritance of Animal class, or we can say the Dog class is the son of Animal class.
**✅ 正确** - 基本理解正确，继承的概念解释清楚

## Question 10
Write a try-except block to handle division by zero error.

A: number = 4

try:

​	number/0

Except ZEROERROR as ze:

​	print("Wrong statement ! 0 can't be the division.")
**❌ 错误**
**你的答案：**
```python
number = 4
try:
    number/0
Except ZEROERROR as ze:
    print("Wrong statement ! 0 can't be the division.")
```
**正确答案：**
```python
number = 10
try:
    result = number / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
```
**错误原因：**
1. 异常类名应该是ZeroDivisionError，不是ZEROERROR
2. Python关键字大小写敏感：except而不是Except
3. 异常处理应该用冒号而不是as ze（除非需要捕获异常对象）

## Question 11
What is the difference between `sorted()` and `.sort()` methods?

A: sorted() method is a default methond of list structure, the .sort() method is a method of List class.
**❌ 错误**
**你的答案：** sorted()方法是列表结构的默认方法，.sort()方法是List类的方法
**正确答案：** 
- sorted()返回新的已排序列表，不影响原列表
- .sort()在原列表上进行排序，返回None
**例子：**
```python
original = [3, 1, 2]
new = sorted(original)  # 返回[1, 2, 3]，original仍为[3, 1, 2]
original.sort()         # original变为[1, 2, 3]，返回None
```

## Question 12
Write a function that uses `*args` to accept any number of arguments and returns their sum.

A: def sum(*args:int):

​	result = 0

​	for i in args:

​		result = result + i

​	return result
**✅ 正确** - 函数实现正确，使用了*args接收可变参数

## Question 13
Explain what sets are and write code to find the intersection of two sets.

A: Sets are a container of all sorts of basic types' variables, you can put int numbers in it , also put str in it, there are some methods allow you to do some useful things to sets.

set1 = (1,2,3,4,5,6,7,8)

set2 = (2,3,4,5,6,7)

 set1.intersection(set2)
**❌ 错误**
**你的答案：** 集合是包含各种基本类型变量的容器
**错误：**
1. 用()创建的是元组，不是集合，应该用{}
2. intersection方法调用正确，但数据结构错误
**正确答案：**
```python
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {2, 3, 4, 5, 6, 7}
result = set1.intersection(set2)  # 或者 set1 & set2
```

## Question 14
Write a context manager using `__enter__` and `__exit__` methods for file operations.

A: file.\_\_enter\_\_()

file.\_\_exit\_\_()
**❌ 错误**
**你的答案：** 直接调用__enter__和__exit__方法
**正确答案：** 实现上下文管理器协议
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
```
**解释：** 上下文管理器需要实现__enter__和__exit__方法，而不是直接调用它们。使用with语句来自动管理资源。

## Question 15

What is the purpose of the `@property` decorator? Provide an example.

A: property decorator is one way to create a property of an class, with @property decorator, you don't need to create a getter or setter for this property, Python will automatically create some simple methods for this property, with these code , you can use a property like using an attribute of an object, instead of calling a method to do something

class A:

​	def \_\_init\_\_(self):

​		self._a = None

​	

​	@property

​	def a(self):

​		return self._a

## Question 16
Write code using dictionary comprehension to create a dictionary where keys are numbers from 1 to 5 and values are their squares.

A: results = {n: n ** 2 for n in range(1,6)}
**✅ 正确** - 字典推导式使用正确。更简洁的写法：
```python
squares = {i: i*i for i in range(1, 6)}
```
**理由：** 变量名更具描述性，使用i*i可能比i**2更直观

## Question 17
Explain the difference between `isinstance()` and `type()` functions.

A: The isinstance() function returns if an object is an instance of class, the type() function will return the type of a variable, if you create a class named A, and you create an object named a,the a is an instance of A class,you should use isinstance() method, if you create a variable like number=1, the type(number) will return the type of number, like int,with using isinstance() method ,you should know a class's name, like A that I mentioned before, if you don't know a name of class, you can't use isinstance() method.
**⚠️ 部分正确但不够准确**
**你的答案：** 基本解释正确，但最后一句话错误
**正确答案：**
```python
# isinstance() 考虑继承关系
class Animal: pass
class Dog(Animal): pass

dog = Dog()
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True（考虑继承）

# type() 不考虑继承
print(type(dog) == Dog)         # True
print(type(dog) == Animal)      # False
```
**解释：** isinstance()返回True如果对象是指定类或其子类的实例，type()只检查确切类型。isinstance()可以检查多个类型：isinstance(x, (int, str))

## Question 18

Write a function that demonstrates polymorphism by having different behaviors for different input types.

A: I really forget how to achieve demonstrates polymorphism in Python.
**❌ 错误 - 无答案**
**解释：** 多态是面向对象编程的重要概念，应该掌握
**正确答案：** 见查漏补缺文件中的多态部分

## Question 19
What are magic methods? Give an example of at least two magic methods.

A: Magic methods are some of the default methods of Python, all classes you created have magic methods, these methods are useful.For example,  \_\_init\_\_() method is the factory method of a class, if you redefine this method, any object that you created from your cumtom class will execute the codes in \_\_init\_\_() method; If you create your own class, and you want to compare two objects of your custom class, you should redefine \_\_eq\_\_() method which is one of the magic methods that defined to show what will happen with "==" condition.
**✅ 正确** - 魔法方法理解基本正确。补充更完整的例子：
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __len__(self):
        return len(self.title)

# 使用
book1 = Book("Python Basics", "John")
print(book1)          # 调用__str__
print(len(book1))     # 调用__len__
```

## Question 20

Write code to import a module and use its functions, demonstrating the `import`, `from`, and `as` syntax.

A: from mymodule import myfunction as func

func()	# use function that I imported
**✅ 正确** - 导入语法正确。补充其他导入方式：
```python
# import module
import math
print(math.sqrt(4))

# import all functions
from math import *
print(sqrt(4))

# import module with alias
import numpy as np
```

---

## 知识点总结与评价

### 1. 函数和参数
**掌握情况：** ✅ 良好
- 默认参数理解正确
- *args使用正确
- lambda概念理解基本正确

**学习建议：** 
- 练习**kwargs的使用
- 学习函数的高级特性

### 2. 面向对象编程
**掌握情况：** ⚠️ 需要改进
- 继承概念理解正确
- 类定义语法错误较多
- 属性装饰器使用正确

**学习建议：** 
- 加强类和实例方法的语法练习
- 理解self的作用
- 练习更多OOP特性

### 3. 异常处理
**掌握情况：** ❌ 严重不足
- 异常类名错误
- 关键字大小写错误
- 异常处理语法不熟练

**学习建议：** 
- 记住常见异常类型
- 练习不同场景的异常处理
- 学习try-except-else-finally结构

### 4. 数据结构操作
**掌握情况：** ⚠️ 需要加强
- 列表方法使用有误
- 集合创建方式错误
- 字典推导式正确

**学习建议：** 
- 练习所有列表方法
- 理解集合的特性
- 学习更多字典操作

### 5. 高级特性
**掌握情况：** ⚠️ 需要加强
- map和filter理解有误
- sorted/sort概念不清
- 上下文管理器不会实现

**学习建议：** 
- 练习函数式编程特性
- 深入理解排序算法
- 实现自定义上下文管理器

### 总体评价
得分：8/20 = 40%
**评价：** 基础概念有一定理解，但语法错误较多，高级特性掌握不足。建议重点练习OOP语法和异常处理。

**错题统计：** 12题错误，主要分布在：
- 语法错误（6题）
- 概念理解错误（4题）
- 不会实现（2题）