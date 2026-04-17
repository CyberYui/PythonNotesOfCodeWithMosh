def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input
    
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
print("-----------------------------")
# Python是一种动态类型语言，这意味着变量不需要声明类型，可以直接赋值使用。
# 在上面的代码中，函数`fizz_buzz`接受一个参数`input`，并根据其值进行判断，返回相应的字符串或数字。
# 我们可以在创建变量后随意赋值不同类型的值，例如：
x = 10  # x是一个整数，整数类型是不可变类型
print(x)  # 输出: 10
print(type(x))  # 输出: <class 'int'>
x = "Hello"  # x现在是一个字符串
print(x)  # 输出: Hello
print(type(x))  # 输出: <class 'str'>
# Python也有类型声明的功能，可以使用类型提示来指定变量的类型
# 但这只是为了代码的可读性和静态分析工具的使用，并不会强制执行类型检查。
y: int = 20  # y被声明为整数类型
print(y)  # 输出: 20
y = "World"  # 这不会引发错误，但会改变y的类型
print(y)  # 输出: World
print(type(y))  # 输出: <class 'str'>
# int y = 15  # 这是C++或Java等静态类型语言的语法，在Python中会引发语法错误

# 通过id函数可以查看变量的内存地址，动态类型语言允许变量指向不同类型的对象
a = 5
print(id(a))  # 输出: 内存地址，例如: 4301105584
a = "Hello"
print(id(a))  # 输出: 不同的内存地址，例如: 4302508528
# 变量指向的内存地址在a被重新赋值后发生了变化，这说明a现在指向了一个新的对象（字符串"Hello"），而不是之前的整数5
# 内存地址不会改变，除非变量被重新赋值指向一个新的对象，一个变量如果被重复赋值同一个值
# 可能会指向同一个内存地址（因为Python会进行小整数缓存），但这并不影响变量的动态类型特性

x= [1, 2, 3]  # x是一个列表，列表是一个可变类型
print(x)  # 输出: [1, 2, 3]
print(type(x))  # 输出: <class 'list'>
print(id(x))  # 输出: 内存地址，例如: 4301105584
x.append(4)  # 修改列表内容
print(x)  # 输出: [1, 2, 3, 4]
print(id(x))  # 输出: 同一个内存地址，例如: 4301105584
# 这说明列表对象本身没有被替换，而是被修改了，因此内存地址保持不变。
# 动态类型语言允许我们在运行时修改对象的内容，而不需要担心类型安全问题，这也是Python等动态类型语言的一个重要特性。