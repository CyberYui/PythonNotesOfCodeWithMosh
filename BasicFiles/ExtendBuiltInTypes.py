# 在我们使用着Python丰富的内置类型时，我们可以通过继承随时拓展他们的功能
# 例如我们想要一个可以复制字符串的方法
class MyString(str):
    def duplicate(self):
        return self + self


# 我们想要在调用列表的append方法时有个提示
class MyList(list):
    def append(self, object):
        print(f"Adding {object} to the list")
        super().append(object)


mystring = MyString("Hello")
print(mystring.duplicate())  # 输出: HelloHello
mylist = MyList()
mylist.append(1)  # 输出: Adding 1 to the list
