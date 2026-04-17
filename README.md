# PythonNotesOfCodeWithMosh

跟随 [Code with Mosh](https://codewithmosh.com/) 的 Python 教程系列学习的笔记与练习文件，所有文件均存放于 `BasicFiles/` 文件夹中，并按照教程的讲解顺序从 01 到 31 依次编号。

---

## 文件列表

| 文件 | 内容简介 |
|------|---------|
| `01_BasicLearning.py` | Python 入门：变量、字符串索引与方法、数值运算、布尔值与 Falsy/Truthy、三元运算符 |
| `02_Numbers.py` | 数字类型详解：十进制、二进制（0b）、十六进制（0x）、复数（j）及相互运算 |
| `03_Strings.py` | 字符串操作详解：索引、切片、步长、拼接、f-string、常用字符串方法 |
| `04_TypeConversion.py` | 类型转换：int()、float()、bool()、str() 的使用，以及 Falsy 值概念 |
| `05_ArithmeticOperations.py` | 算术运算：加减乘除、整除、取余、幂运算、复合赋值运算符、math 模块 |
| `06_ConditionalStatements.py` | 条件语句：if/elif/else、比较运算符、逻辑运算符（and/or/not）、三元运算符 |
| `07_BasicLoop.py` | 基础循环：for 循环遍历字符串和列表、range() 函数、for-else、while 猜数字游戏 |
| `08_Loops.py` | 循环进阶：range 详解、for-else、while-else、continue、break，以及猜数字游戏示例 |
| `09_SwappingVariables.py` | 变量交换：利用元组打包/解包一行实现两个（或多个）变量值的互换 |
| `10_Lists.py` | 列表详解：创建、索引、切片、解包、enumerate、增删改查、排序、lambda、map、filter、列表推导式、zip |
| `11_Tuples.py` | 元组详解：不可变序列的创建方式、索引、切片，与列表的区别 |
| `12_Arrays.py` | 数组（array 模块）：类型码、append、pop、insert，与 list 的性能对比概念 |
| `13_Sets.py` | 集合（Set）：创建、add/remove、并集/交集/差集/对称差集，以及唯一性特性 |
| `14_DictionariesAndGenerators.py` | 字典详解：创建、访问、增删、遍历、keys/values/items；列表/集合/字典推导式；生成器表达式及内存优势 |
| `15_UnpackingOperator.py` | 解包运算符（* 和 **）：解包列表/字典、合并可迭代对象，以及统计字符串字母频率的综合练习 |
| `16_BasicFunction.py` | 函数详解：定义、位置参数与关键字参数、默认参数、类型注解、*args、**kwargs、作用域与 global |
| `17_Exercise.py` | 函数练习：FizzBuzz 实现；动态类型语言特性：类型提示、id() 与可变/不可变对象 |
| `18_VariableWarning.py` | 变量作用域：局部变量、全局变量、global 关键字的使用与注意事项 |
| `19_Debugging.py` | 调试技巧：使用 VSCode 断点（F9/F5/F10/F11）逐步调试 Python 程序 |
| `20_Exceptions.py` | 异常处理：try/except/else/finally、捕获多种异常、with 语句、自定义异常、raise、timeit 性能对比 |
| `21_Classes.py` | 面向对象编程（类）：类定义、实例属性与类属性、__init__、__str__、类方法（@classmethod）、魔法方法（__eq__、__gt__、__add__） |
| `22_Inheritance.py` | 继承：单继承、多重继承、super()、方法覆写、isinstance/issubclass、抽象类（ABC）、多态与 Duck Typing |
| `23_Properties.py` | 属性（Properties）：@property 装饰器与 @setter 的 Pythonic 用法，避免暴露多余方法 |
| `24_ExtendBuiltInTypes.py` | 扩展内置类型：通过继承 str 和 list 为内置类型添加自定义方法 |
| `25_CustomContainer.py` | 自定义容器：实现 __getitem__、__setitem__、__len__、__iter__ 魔法方法，大小写不敏感的 TagCloud |
| `26_DataClasses.py` | 数据类：使用 namedtuple 创建不可变数据类，使用 @dataclass 装饰器创建可变数据类 |
| `27_Modules.py` | 模块与导入：模块概念、import 的最佳实践（避免 *），以及用 importlib 动态加载模块的示例 |
| `28_ModuleSales.py` | 模块示例：为 27_Modules.py 提供 calc_tax、calc_shipping 等演示函数的配套模块文件 |
| `29_Stacks.py` | 栈（Stack）：LIFO 结构，用 Python list 的 append/pop 模拟栈的入栈与出栈 |
| `30_Queues.py` | 队列（Queue）：FIFO 结构，使用 collections.deque 实现高效的双端队列操作 |
| `31_AIspeedTest.py` | AI 推理速度测试：使用 mlx-lm 在本地 GPU 上加载并测试大语言模型的 token 生成速度（个人实验文件） |

---

## 学习资源

- [Code with Mosh - Python for Beginners](https://www.youtube.com/watch?v=kqtD5dpn9C8)
- [Code with Mosh - Python Intermediate](https://codewithmosh.com/p/python-programming-course-beginners)
