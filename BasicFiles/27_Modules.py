# 在我们真正开发程序时，代码会变得非常复杂。为了让代码更易于维护，我们需要将代码分成不同的文件。
# 这些文件被称为模块。比如和当前文件同目录下的 28_ModuleSales.py 就是一个演示模块的文件。
# 在实际项目中，模块文件名应该是合法的 Python 标识符（不以数字开头），例如 sales.py 或 module_sales.py。
# 为了方便演示，下面用 importlib 来加载重命名后的模块文件。

# 在引用模块的时候，尽量不要使用*引用全部方法，因为对于使用模块的人来说，他们并不知道这个模块中有哪些方法
# 使用*有可能会导致模块中的方法名和当前文件中的方法名冲突，导致程序出错
# from ModuleSales import *

# 尽量引用特定的方法，或者直接使用import来引用一个模块对象，这样也可以引入整个模块的内容，只是需要通过模块对象调用

# 原始示例代码（模块文件命名为 ModuleSales.py 时）：
# from ModuleSales import calc_tax, calc_shipping
# import ModuleSales
# calc_tax()
# calc_shipping()
# ModuleSales.calculate_sales_tax()
# ModuleSales.calculate_total_sales()

# 由于模块文件已重命名为 28_ModuleSales.py（以数字开头，不是合法的 Python 模块名），
# 这里使用 importlib 来动态加载该模块文件进行演示
# importlib 是 Python 的一个标准库模块，提供了用于动态加载模块的功能
# 我们可以使用它来加载任何指定路径的 Python 文件作为模块
import importlib.util

# os 模块提供了与操作系统进行交互的功能，这里我们用它来构建模块文件的路径
import os

# 构建模块文件的路径，并使用 importlib 来加载模块文件
module_path = os.path.join(os.path.dirname(__file__), "28_ModuleSales.py")
spec = importlib.util.spec_from_file_location("ModuleSales", module_path)
# 创建模块对象并执行模块代码
ModuleSales = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ModuleSales)

# 对于单独引用的方法，我们可以直接调用它们
ModuleSales.calc_tax()
ModuleSales.calc_shipping()
# 对于通过import引用的模块，我们需要通过模块对象来调用它们的方法
ModuleSales.calculate_sales_tax()
ModuleSales.calculate_total_sales()
