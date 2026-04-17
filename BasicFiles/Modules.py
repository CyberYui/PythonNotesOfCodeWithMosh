# 在我们真正开发程序时，代码会变得非常复杂。为了让代码更易于维护，我们需要将代码分成不同的文件。
# 这些文件被称为模块。比如和当前文件同目录下的ModuleSales.py就是一个模块。我们可以在当前文件中导入这个模块来使用它的功能。
# 在引用模块的时候，尽量不要使用*引用全部方法，因为对于使用模块的人来说，他们并不知道这个模块中有哪些方法
# 使用*有可能会导致模块中的方法名和当前文件中的方法名冲突，导致程序出错
# from ModuleSales import *
# 尽量引用特定的方法，或者直接使用import来引用一个模块对象，这样也可以引入整个模块的内容，只是需要通过模块对象调用
from ModuleSales import calc_tax, calc_shipping
import ModuleSales

# 对于单独引用的方法，我们可以直接调用它们
calc_tax()
calc_shipping()
# 对于通过import引用的模块，我们需要通过模块对象来调用它们的方法
ModuleSales.calculate_sales_tax()
ModuleSales.calculate_total_sales()
