# 在实际的编程中，你可能会遇到一些只存储了数据的类，这些类通常被称为数据类（Data Classes）
# 数据类里面通常只包含一些属性，没有方法，或者只有一些简单的方法来操作这些属性
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# 我们在使用类时也没有问题，但是当我们比较两个对象时，结果可能会不尽人意
p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # 输出: False
# 这也很好理解，实际上对比的是两个对象的内存地址，而不是它们的属性值
# 在之前学习中我们知道，如果我们想要比较两个对象的属性值，我们需要重写__eq__方法
print(p1 == p2)  # 输出: True

# 但是事实上在一个数据类中写入方法这件事本身就很违和
# 我们只是想要一个简单的类来存储数据，而不是一个复杂的类来处理数据
# 我们也不想每次为了实现几个数据的比较或者打印功能就要去重写一个魔法方法
# 我们可以通过引入namedtuple来解决这个问题
from collections import namedtuple

# namedtuple是一个工厂函数，它可以用来创建一个简单的类，这个类有一些属性，并且自动实现了一些方法，比如__eq__和__repr__
# 相比于我们自己写一个类，使用namedtuple可以让我们更快地创建一个数据类，并且不需要担心实现一些基本的方法
Point = namedtuple("Point", ["x", "y"])
# 在创建变量时，为了使代码便于阅读，我们应该直接使用属性名来赋值，而不是按照位置来赋值
p3 = Point(x=1, y=2)
p4 = Point(x=1, y=2)
print(p3 == p4)  # 输出: True
# 通过namedtuple创建的类还自动实现了__repr__方法，就像我们自己创建的自定义类一样
# 我们也可以直接访问属性，而不需要担心它们的内存地址
print(p3.x)  # 输出: 1
print(p3.y)  # 输出: 2
# 唯一需要注意的是，namedtuple创建的类是不可变的，也就是说我们不能修改它们的属性值
# 这也是为什么我们在创建变量时需要直接使用属性名来赋值的原因
# 如果我们需要一个可变的数据类，我们可以使用dataclass来创建一个数据类
from dataclasses import dataclass


# 创建数据类非常简单，我们只需要使用@dataclass装饰器来装饰一个类，并且在类中定义一些属性就可以了
# 与其他类不同的是，我们不再需要定义方法，只需要定义属性就可以了，dataclass会自动为我们生成一些方法，比如__eq__和__repr__等
@dataclass
class PointData:
    x: int
    y: int


# 创建变量的方式没有什么不同，我们仍然可以直接使用属性名来赋值，也可以按照位置来赋值
p5 = PointData(x=1, y=2)
p6 = PointData(x=1, y=2)
p7 = PointData(1, 2)
print(p5 == p6)  # 输出: True
print(p5.x)  # 输出: 1
print(p5.y)  # 输出: 2
print(p7)  # 输出: PointData(x=1, y=2)
# dataclass创建的类默认是可变的，也就是说我们可以修改它们的属性值
p5.x = 3
print(p5.x)  # 输出: 3
# dataclass创建的类还自动实现了__repr__方法，就像我们自己创建的自定义类一样
print(p5)  # 输出: PointData(x=3, y=2)
