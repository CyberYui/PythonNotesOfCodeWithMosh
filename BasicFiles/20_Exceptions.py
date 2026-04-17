# 在使用Python编程时，我们经常会遇到报错和异常
# 这些错误和异常可能会导致程序崩溃或者无法正常运行
# 为了在合适的时机抓取异常并加以利用，我们可以使用try-except语句来处理异常
try:
    age = int(input("请输入你的年龄: "))
    x = (
        10 / age
    )  # age为0时会引发ZeroDivisionError异常，age为非整数时会引发ValueError异常
    # 有时候我们还会使用with语句来处理文件等资源，这样可以确保资源在使用完毕后被正确地释放
    # 在打开一个文件的时候，尽量使用enconding参数来指定文件的编码格式，这样可以避免在读取文件时出现编码错误
    with open("file.txt", "r", encoding="utf-8") as file:
        print("文件打开成功！")
        content = file.read()
    # with语句会自动释放资源，这是如何实现的呢？其实with语句背后是通过上下文管理器来实现的
    # 在这里，有两个函数需要特别注意，即__enter__和__exit__，它们分别在with语句开始和结束时被调用
    # __enter__函数会在with语句开始时被调用
    # 它的返回值会被赋值给as后面的变量，这样我们就可以在with块中使用这个变量来操作资源了
    # __exit__函数会在with语句结束时被调用，无论是正常结束还是由于异常而结束__exit__函数都会被调用
    # 这样我们就可以在__exit__函数中进行资源的清理工作了，比如关闭文件等
    # file.__enter__()  # 打开文件
    # 在这里我们可以对文件进行操作，比如读取文件内容等
    # file.__exit__(None, None, None)  # 关闭文件

    # 对于这种有__enter__和__exit__方法的对象
    # 我们称这种对象为context management object（上下文管理器对象），它们可以被with语句使用来管理资源的使用和释放
    # 我们也称这类对象满足context management protocol（上下文管理协议）就是指__enter__和__exit__方法的规范
    # 这个规范定义了如何在with语句中使用上下文管理器对象来管理资源的使用和释放

# 当有异常的时候，except块中的代码会被执行，我们可以在这里处理异常，比如提示用户输入错误或者记录日志等
# 实际上异常还可以被我们存成一个变量，以便我们在except块中使用它来获取更多的异常信息
# except ValueError:    # 这种写法只能捕获ValueError类型的异常，但无法获取异常的具体信息
except ValueError as e:
    print(e)
    print(type(e))
    print(f"发生了一个未知的错误: {e}")
    print("输入的年龄必须是一个整数！")
    # 这里我们捕获了ValueError类型的异常，并打印出异常信息
    # 实际上我们还可以捕获更多的异常
except ZeroDivisionError as e:
    print(e)
    print(type(e))
    print(f"发生了一个未知的错误: {e}")
    print("除数不能为零！")
# 当我们想同时抓取多种异常，并输出相同内容时，可以使用元组来捕获多个异常
# 实际上Python在处理异常时是从上到下依次检查的
# 如果某个except块中的异常类型与发生的异常类型匹配
# 那么就只会执行该except块中的代码，并且不会继续检查后面的except块了
except (ValueError, ZeroDivisionError) as e:
    # 这段内容会被程序忽略，因为前面已经有了针对两种异常的except块了
    print(f"发生了一个未知的错误: {e}")
else:
    print("输入的年龄没有问题！")
    print(f"你的年龄是: {age}")
    # 如果try块中的代码没有发生任何异常，那么else块中的代码会被执行
finally:
    print("无论是否发生异常，这段代码都会被执行！")
    # finally块中的代码无论是否发生异常都会被执行，通常用于清理资源或者执行一些收尾工作
    # with语句会自动管理资源的释放，所以在使用with语句处理文件时，我们不需要手动关闭文件
    # 但为了演示finally块的作用，这里还是手动关闭了文件
    try:
        file.close()
    # 由于file是在try块中定义的，如果try块中的代码发生了异常
    # 那么file就不会被定义，这时在finally块中访问file就会引发NameError异常
    # 因此我们需要在finally块中捕获这个异常，以避免程序崩溃
    except NameError as e:
        print(e)
        print(type(e))
        print(f"发生了一个未知的错误: {e}")
        print("文件对象不存在，无法关闭文件！")


# 实际上我们不仅仅能抓取已经被定义的异常类型，还可以自定义异常类型来满足我们特定的需求
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("年龄必须是一个正数！")
    return 10 / age


# 当我们使用此函数，并传入一个满足if判断的值时，就会弹出我们自定义的异常
try:
    calculate_xfactor(-5)
except ValueError as error:
    print(error)
    print(type(error))
    print(f"发生了一个错误: {error}")

# 当我们使用raise语句的时候，一定要三思而后行，除非必要，否则尽量不要使用raise语句引出异常
# 当我们的代码能正常运行时，带有raise的代码虽然能在控制台输出异常信息
# 但是它的速度会比正常的代码慢很多，因为引发异常需要进行一些额外的处理工作，比如创建异常对象、查找异常处理程序等
# 所以除非你不得不使用raise语句，否则尽量不要使用它
# 我们可以通过引用timeit模块来测试一下引发异常的代码和正常代码的运行速度
from timeit import timeit

# code1是之前抓取异常并使用了raise语句的代码
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("年龄必须是一个正数！")
    return 10 / age

try:
    calculate_xfactor(-5)
except ValueError as error:
    print(error)
"""
# code2是不抓取异常，直接进行判断的代码
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-5)
if xfactor == None:
    pass
"""
# 对比两个代码的速度，会发现code1的速度比code2的速度慢4倍
# timeit的第二个参数是执行次数，这里我设置为了10000次
print(timeit(code1, number=10000))  # 0.027984542
print(timeit(code2, number=10000))  # 0.0009470410000000928
