"""这个练习是为了理解Debugging的概念"""


def multiply(*numbers):
    """这个函数接受任意数量的数字，并返回它们的乘积"""
    total = 1
    for number in numbers:
        total *= number
    return total


# 使用f9设置断点，调试这个程序，就可以看到每一步的执行过程，这能帮我们理解程序的运行方式，并找到潜在的错误
# 断点不再在终端中使用，而是使用debug面板，例如VScode中可以通过点击行号设置断点，或者使用快捷键F9来设置断点
# 点击运行调试模式后会自动创建一个launch.json文件，这个文件包含了调试配置，可以根据需要进行修改
# 例如指定要调试的Python文件，设置环境变量等，但是现在我们不需要操作它，直接跳过这个文件运行调试模式就可以了
# 设置断点后，运行调试模式（通常是按F5），程序会在断点处暂停，这时你可以检查变量的值，查看调用堆栈，逐步执行代码等
print("starting the program...")
# 通过F10逐行继续代码，在运行到函数阶段，按F11进入函数内部，然后继续按F10就能查看函数的执行过程了
# 我的VScode会直接在行内显示变量值和计算公式的变化，如果你的没有，那可以在左侧的Watch面板中添加total来观察
print(multiply(2, 3, 4))
print("ending the program...")

# 在视频https://www.bilibili.com/video/BV1MXBRY6EU8/?spm_id_from=333.1391.0.0&p=2&vd_source=ee48d919e337532424f8e2f7080b7adf
# 中，Mosh在1：06：31处展示了一些使用VScode的技巧，例如框选两行，使用Alt+方向键来移动该行位置
# 如果是Mac系统，那么从1：08：36开始看即可
