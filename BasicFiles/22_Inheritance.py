from abc import ABC, abstractmethod


# 当你创建了很多类之后，你会发现它们之间有很多相似之处，比如骆驼类和狮子类都有吃和走的方法
# 由此我们想到可以创建一个动物类，把这些相似的方法放在这个类里
# 这种想法很正常，因为当你创建了很多个相同的方法在不同的类中，一旦有一次这个方法出现了bug
# 那么你要将所有有这个方法的地方都修改，这就十分麻烦了
# 这引出了编程中的DRY（Don't Repeat Yourself）原则，意思是不要重复自己
# 所以骆驼类和狮子类都应该基于这个动物类，再去创建新内容，这样它们就可以使用动物类里的方法了
# 而一旦这个方法出错，我们不需要修改骆驼类和狮子类，只需要修改动物类就可以了，这样就大大减少了工作量
# 这种创建新类的方式叫做继承，骆驼类和狮子类称为动物类的子类，动物类称为它们的父类
# 实际上为了避免重复代码，还有组合(Composition)的概念
# 组合是指一个类包含另一个类的实例作为它的属性，这样就可以重用那个类的功能，而不需要继承它，后面会讲到
# 回到继承，我们可以通过在子类的定义中指定父类来实现继承
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

    def walk(self):
        print("walk")


# 通过在子类的定义中指定父类，我们就可以让子类继承父类的属性和方法了
class Camel(Animal):
    def __init__(self):
        self.weight = 20

    def humps(self):
        print("humps")


class Lion(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 30

    def roar(self):
        print("roar")


# 下面两个类(Employee & Person)用于多重继承的例子
class Employee:
    def work(self):
        print("work")

    def greet(self):
        print("Employee greet")


class Person:
    def eat(self):
        print("eat")

    def greet(self):
        print("Person greet")


# 当我们创建一个骆驼对象时，它就会自动继承动物类的eat和walk方法了
camel = Camel()
camel.eat()  # eat
camel.walk()  # walk
camel.humps()  # humps
# 同样的，当我们创建一个狮子对象时，它也会自动继承动物类的eat和walk方法了
lion = Lion()
lion.eat()  # eat
lion.walk()  # walk
lion.roar()  # roar

# 事实上现实生活中的继承类不会像我们做的这么简单，使用动物类和子类只是方便举例
# 对于类中的构造函数，比如上面我们在Animal类中定义了__init__方法
# 如果我们在子类也定义这个方法，你会发现父类的方法会失效
# print(camel.age)  # AttributeError: 'Camel' object has no attribute 'age'
print(lion.age)  # 1
print(camel.weight)  # 20
# 这是一种典型的函数覆写现象，那么如果我们既要父类的方法内容，又要子类的方法内容的话
# 就需要借助super函数了，就像上面Lion类中写的那样
print(lion.age)
print(lion.weight)

# 为了防止程序出现错误，一般建议类的继承层级控制在三层以内，过多的继承层级会让程序变得复杂难以维护
# 你可以通过使用isinstance函数来检查一个对象是否是某个类的实例，或者是某个类的子类的实例
print(isinstance(camel, Camel))  # True
# 你也可以通过使用issubclass函数来检查一个类是否是另一个类的子类
print(issubclass(Camel, Animal))  # True


# 需要注意的是，一个子类是可以继承多个父类的，这叫做多重继承，不过在实际开发中我们很少使用多重继承，因为它会让程序变得复杂难以维护
# 例如Manager类同时继承了Employee和Person类
class Manager(Employee, Person):
    pass


# 当我们创建一个manager对象时，它就会同时继承Employee和Person类的方法了
manager = Manager()
manager.work()  # work
manager.eat()  # eat
# 但是当我们调用greet方法时，程序会优先调用Employee类中的greet方法，因为在Manager类中Employee类被放在了Person类的前面
manager.greet()  # Employee greet


# 既然多重继承一般会导致程序复杂，Python中为什么还要有这个特性呢？
# 因为在一些特定时刻，多重继承会十分有用，比如当你需要创建一个类来组合多个类的功能时，多重继承就可以派上用场了
class flyingAnimal:
    def fly(self):
        print("I can fly~")


class swimmingAnimal:
    def swim(self):
        print("I can swim!")


class Duck(flyingAnimal, swimmingAnimal):
    pass


# 你可以看到，鸭子刚刚好是一个既会飞又会游泳的动物
# 所以我们就可以通过多重继承来创建一个Duck类来组合flyingAnimal和swimmingAnimal的功能了
duck = Duck()
duck.fly()  # I can fly~
duck.swim()  # I can swim!

print("------------------")


# 在很多时候，我们会想要程序帮我们做一些事情，比如帮我们读取文件，甚至流式传输文件
# 根据这个背景，我们可以创建一个继承的良好例子
# 我们通过继承相关的知识来创建一个新的类，来实现流的读取等功能
# 我们首先创建一个Stream类来模拟流式传输文件的功能，这个类有一个open方法和一个close方法
# 为了判断流是否已经打开了，我们还定义了一个opened属性来记录流的状态
# 然后我们还定义了一个自定义异常类，它会在文件没有被正确操作时抛出异常，这样就可以让程序更健壮了
class InvalidOperationError(Exception):
    pass


# Stream类作为流类来模拟流式传输文件的功能，这个类有一个open方法和一个close方法
"""
class Stream:
    def __init__(self, name):
        self.name = name
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        else:
            self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        else:
            self.opened = False
"""


# 为了使Stream类成为一个抽象类，我们需要让它继承ABC类，并且将read方法定义为一个抽象方法，这样就可以强制要求所有继承Stream类的子类都必须实现read方法了
class Stream(ABC):
    def __init__(self, name):
        self.name = name
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        else:
            self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        else:
            self.opened = False

    @abstractmethod
    def read(self):
        pass


# 现在我们想要创建一个FileStream类来模拟文件流的功能，这个类应该继承Stream类，因为它也需要有打开和关闭流的功能
# 我们要知道，从一个文件读取数据和从一个网络流读取数据是有区别的，读取文件我们会用到FileStream类，然后它可能覆写Stream类中的方法从而实现不同的功能
class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


# 同样的我们还需要一个NetworkStream类来模拟网络流的功能，这个类也应该继承Stream类，并且有一些其他的功能
class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network stream")


# 当我们要创建一个抽象类的空继承类时，由于没有read方法的实现，所以会在创建对象时抛出异常，因为类中的抽象方法read没有被实现
# class MemoryStream(Stream):
#     pass
# memorystream = MemoryStream("memory stream")  # TypeError: Can't instantiate abstract class MemoryStream with abstract method read
class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory stream")


# 这就是一个很正常的继承关系，FileStream和NetworkStream都继承了Stream类，并且结构清晰，没有超过三层的继承层级


# 在实际使用中会有个问题，比如我们创建了Stream类对象，但是当我们要调用open方法的时候，是要打开一个文件流还是一个网络流呢？
# 也就是说我们应该从继承了Stream类的FileStream和NetworkStream类中去创建对象，而不是直接从Stream类中去创建对象
# 但是这样会有个新问题，FileStream和NetworkStream类中都有一个read方法，是否可以将两个类中的read方法放在Stream类中呢？
# 但是如果放在Stream类中，那么它们就会有类似的实现了，这样就又回到了刚刚的问题，程序如何判断应该调用哪个read方法
# 这时候我们就需要使用抽象类了，抽象类是一种特殊的类，它不能被实例化，只能被继承
# 一般通过引入abc模块中的ABC类和abstractmethod装饰器来实现抽象类和抽象方法
# 抽象类中可以定义一些抽象方法，这些方法在抽象类中没有具体的实现，而是由子类来实现的，这样就可以解决继承带来的此类问题
# 在这个例子中，流这个类就是一种抽象的概念，正好可以使用抽象类来实现
# 将Stream类定义为一个抽象类，并且将read方法定义为一个抽象方法，这样就可以强制要求所有继承Stream类的子类都必须实现read方法了
# stream = Stream()  # TypeError: Can't instantiate abstract class Stream with abstract method read
# 现在我们解决了只通过子类创建对象的问题，那么关于read方法的调用问题，我们就可以通过多态(Polymorphism)来解决了
# 多态是指同一个方法在不同的对象上有不同的表现形式，这样就可以通过调用同一个方法来实现不同的功能了，这也是面向对象编程的一个重要特征
# 下面是一个多态的例子
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# 到这里其实和之前没什么不同，我们有FileStream和NetworkStream类并且都实现了read方法
# 现在我们又有了TextBox和DropDownList类继承于抽象类UIControl并且都实现了draw方法
# 下面，我们要让程序去决定调用哪个类的draw方法
def draw(controls):
    # draw方法不知道传入的是什么类型的对象
    # 它只知道它们都是UIControl类的子类，并且都实现了draw方法
    # 所以它就简单地调用draw方法，但是每种对象都有对应的输出，这就是多态的体现了
    for control in controls:
        control.draw()


# 我们会传入一个包含多个UIControl对象的列表，程序会根据对象的类型来调用相应的draw方法，这就是多态的体现了
textbox = TextBox()
dropdownlist = DropDownList()
draw([textbox, dropdownlist])  # 不同类型的对象调用同一个方法，表现出不同的行为

print("------------------")


# 在Python中我们有个叫Duck Typing的概念，意思是如果一个对象看起来像鸭子，叫起来像鸭子，那么它就是鸭子了
# 也就是说在Python中，我们不需要关心一个对象的类型，只要它有我们需要的方法就可以了，这也是Python的一大特点了
# 这也是为什么我们在上面的draw函数中没有对传入的对象进行类型检查的原因了，因为我们只关心它们是否实现了draw方法，而不关心它们的具体类型
# 有意思的是，当我们没有UIControl这个抽象类的时候，我们也可以通过draw函数来实现多态的效果了
# 因为Python是动态类型语言，所以只要传入的对象有draw方法就可以了，这也是Duck Typing的体现了
# 而在其他的程序语言中，如果没有抽象类或者接口的话，那么就无法实现多态了，因为它们是静态类型语言，所以必须要有一个共同的父类或者接口来实现多态
# 比如我们创建Button类和RadioButton类，它们都有一个draw方法，但是并不继承UIControl类了，我们依然可以通过draw函数来实现多态
class Button:
    def draw(self):
        print("Button")


class RadioButton:
    def draw(self):
        print("RadioButton")


button = Button()
radiobutton = RadioButton()
draw(
    [textbox, dropdownlist, button, radiobutton]
)  # 不同类型的对象调用同一个方法，表现出不同的行为
