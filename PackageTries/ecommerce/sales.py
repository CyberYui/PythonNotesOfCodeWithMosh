def calc_tax():
    print("Calculating tax from ecommerce.sales")


def calc_shipping():
    print("Calculating shipping from ecommerce.sales")


# 当这个模块被直接运行时，__name__的值为"__main__"
# 当这个模块被导入时，__name__的值为模块的名字，即"ecommerce.shopping.sales"
if __name__ == "__main__":
    print("Sales module is being run directly")
    calc_tax()
