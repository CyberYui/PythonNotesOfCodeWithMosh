"""
Code with Mosh - Packages section practice

This file demonstrates:
1) Creating and importing a package
2) Using sub-packages
3) Intra-package imports
4) Inspecting module/package members with dir()
"""

# 1) Import package module directly
import ecommerce.sales

ecommerce.sales.calc_shipping()
ecommerce.sales.calc_tax()

# 2) Import specific functions from a module
from ecommerce.sales import calc_shipping

calc_shipping()

# 3) Alias import
from ecommerce.sales import calc_tax as tax

tax()

# 4) Import from a sub-package module
# absolute path import
from ecommerce.shopping.sales import calc_package_shipping

# relative path import (works only within the package)
# from ..ecommerce.shopping.sales import clac_package_shipping

calc_package_shipping()

# 5) Intra-package references in action
from ecommerce.shopping.sales import calc_shipping_and_notify

calc_shipping_and_notify()

# 6) Inspect package/module attributes with dir()
print(dir(ecommerce))
print(dir(ecommerce.sales))
from ecommerce.shopping import sales

# There are many magic methods that we can try to use
print(sales.__name__)  # It'll print the name of the module
print(sales.__file__)  # It'll print the path to the file where the module is defined
print(sales.__package__)  # It'll print the name of the package that contains the module
