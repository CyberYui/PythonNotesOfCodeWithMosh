# 和其他的程序语言一样，学完类之后自然而然就会想到封装，想到属性(Properties)
# 如果是其他语言基础的程序员，可能会写出这样的代码：
"""
class Product:
    def __init__(self, price):
        # 为了防止直接初始化价格属性，我们在这里调用了一个方法来设置价格
        # 这个方法会检查价格是否合法，如果不合法就抛出一个异常
        # 还有个好处是，我们直接在方法里设置了私有属性，这样就不能直接访问了
        self.set_price(price)

    def set_price(self, price):
        if price < 0:
            raise ValueError("价格不能为负数")
        self.__price = price

    def get_price(self):
        return self.__price

    # 事实上当像这样创建好类之后，你有一个简单的方式来实现优雅的调用效果
    # 那就是在创建属性的时候，使用property函数来创建一个属性，这个属性会自动调用get_price和set_price方法
    price = property(get_price, set_price)

product = Product(-10)
# 取值时通过方法调用
print(product.get_price())
# 赋值时也通过方法调用
product.set_price(200)
# price属性创建时已经绑定了get_price和set_price方法，所以我们可以直接访问price属性来获取和设置价格
# 可以看到虽然get_price和set_price是作为方法被定义的，但是使用时我们却可以当成属性来访问，这就是property函数的作用
# 而这种将方法变成属性的效果，这种属性叫Property，而不是attribute
print(product.price)  # 200
# product.get_price()这种代码实际上在污染我们的接口对象
# 因为它暴露了一个不必要的方法，这个方法只是为了实现属性而存在的
# 而不是为了提供一个功能性的接口，所以它会让用户觉得这个类的接口很乱，或者说不够优雅
"""


# 这类代码当然能使用，甚至在一些规矩不清晰的程序中被大量使用，但是用这种写法，和用其他程序语言开发没有差别
# 你花了大量时间，只是从C++或者Java的习惯里，写了一个相似的冗长的Python代码
# 这在Python里是不够Pythonic（Pythonic指符合Python语言风格的），是不够优雅的代码
# 在Python里，我们有一个更简单的方式来实现这种方法变属性的效果，那就是使用@property装饰器
# 使用@property装饰器，我们可以把一个方法变成一个属性，调用时也会很方便
# 从之前的p.get_price()变成p.price，也就是说可以直接访问，而不需要调用方法
class Product:
    def __init__(self, price):
        # 当我们设置了property装饰器之后
        # 我们就不需要再通过set_price方法设置属性了
        # 我们可以直接在price属性上设置价格
        self.price = price

    # 添加@property装饰器会把这个方法变成一个属性
    @property
    def price(self):
        return self.__price

    # 添加@price.setter装饰器会把这个方法变成price属性的setter方法
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("价格不能为负数")
        self.__price = value


# 如果我们使用property()函数创建属性的话，在使用属性.的时候
# 你会看到对应的get_price和set_price方法，这种方法的暴露会让用户觉得这个类的接口很乱，或者说不够优雅
# 试想一下一个遥控器有50个按钮，如果每个按钮都暴露着一个不必要的方法
# 那么这个遥控器就会变得非常混乱，用户也不知道该按哪个按钮了
# 所以一般来说我们不会在类中通过property()函数来创建属性
# 而是使用@property装饰器来创建属性，这样就不会暴露出不必要的方法了
# 相应的，通过@property装饰器创建的属性，需要通过@属性名.setter装饰器来创建setter方法，这样就可以直接通过属性名来设置属性了
product = Product(10)
print(product.price)  # 10
product.price = 20
print(product.price)  # 20
# product.price = -10  # ValueError: 价格不能为负数
# 这种创建类的形式在程序抛出AttributeError异常时会更优雅一些，因为它不会暴露出不必要的方法来污染接口对象
# 比如你将上面代码中的setter方法注释掉之后，再尝试设置价格属性
# 就会抛出AttributeError异常，而不是ValueError异常，这样就更符合Python的风格了
