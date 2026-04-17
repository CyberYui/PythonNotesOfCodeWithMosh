# Code With Mosh - Packages 笔记

## 1. 为什么需要 Package
- 当模块（module）越来越多时，把相关模块放在一个目录里更易管理。
- 这个目录就是 package。
- package 的本质是一个包含 `__init__.py` 的文件夹，Python会自动将其理解为一个 package

---

## 2. 创建第一个包：ecommerce

根据之前的例子，我们有一个 `sales.py` 模块，里面有两个函数：`calc_tax` 和 `calc_shipping`。我们把它放在一个叫 `ecommerce` 的目录里，这个目录就可以作为一个 package。
目录结构（初始阶段）：

```text
PackageTries/
  app.py
  ecommerce/
    __init__.py
    sales.py
```

`ecommerce/sales.py` 示例：

```python
def calc_tax():
    print("Calculating tax from ecommerce.sales")

def calc_shipping():
    print("Calculating shipping from ecommerce.sales")
```

---

## 3. 在 app.py 中导入包/模块

我们有多种方式导入模块中的函数：

### 3.1 直接导入模块

```python
import ecommerce.sales

ecommerce.sales.calc_shipping()
ecommerce.sales.calc_tax()
```

特点：通过完整路径(absolute path)调用函数，清晰但冗长
- 最清晰，能看出函数来自哪个模块
- 调用时较长（需要写完整路径）

### 3.2 导入指定函数

```python
from ecommerce.sales import calc_shipping

calc_shipping()
```

特点：通过函数名直接调用，简洁但不够明确
- 使用时写法更短
- 来源不如完整模块路径直观

### 3.3 别名导入

```python
from ecommerce.sales import calc_tax as tax

tax()
```

特点：能够给函数起一个更短的名字，适合频繁调用的函数
- 简化调用。
- 适合模块名或函数名过长的场景。

### 3.4 使用相对路径导入

```python
from ..ecommerce.sales import calc_shipping

calc_shipping()
```

特点：在包内模块之间导入时使用，表示从当前模块所在的包开始查找
- 适用于包内模块互相调用的情况。
- 需要注意相对路径的层级关系，容易出错。

---

## 4. 创建子包（sub-package）

为了演示，将 ecommerce 包继续拆分，增加两个子包：`customer` 和 `shopping`。

目录结构（子包阶段）：

```text
PackageTries/
  app.py
  ecommerce/
    __init__.py
    sales.py
    customer/
      __init__.py
      contact.py
    shopping/
      __init__.py
      sales.py
```

`ecommerce/customer/contact.py`：

```python
def contact_customer():
    print("Contacting customer from ecommerce.customer.contact")
```

`ecommerce/shopping/sales.py`：

在这里使用了相对路径导入 `contact_customer` 函数：

```python
from ..customer.contact import contact_customer

def calc_package_shipping():
    print("Calculating shipping from ecommerce.shopping.sales")

def calc_shipping_and_notify():
    calc_package_shipping()
    contact_customer()
```

说明：

- `..customer.contact` 是相对导入，表示从当前子包 `shopping` 回到上一级 `ecommerce`，再进入 `customer.contact`。
- 这就是包内模块互相调用（intra-package references）的常见方式。

---

## 5. 在 app.py 中调用子包模块

```python
from ecommerce.shopping.sales import calc_package_shipping
from ecommerce.shopping.sales import calc_shipping_and_notify

calc_package_shipping()
calc_shipping_and_notify()
```

运行结果会体现两步：

1. 计算 shipping
2. 通知 customer

---

## 6. 介绍 dir()

`dir()` 用来查看对象可用的成员（属性、函数、类等）。

示例：

```python
import ecommerce
import ecommerce.sales

print(dir(ecommerce))
print(dir(ecommerce.sales))
```

你会看到：

- 包对象里的内置属性（例如 `__name__`, `__package__`, `__path__`）
- 模块中定义的函数（例如 `calc_tax`, `calc_shipping`）

这一步通常用于：

- 快速探索一个模块里有什么可用成员
- 调试导入是否成功

