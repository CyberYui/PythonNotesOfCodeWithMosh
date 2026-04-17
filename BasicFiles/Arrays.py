# 当我们针对大量数据进行操作时，仅仅使用列表和元组的简单函数是无法满足排序等操作的
# 在90%的情况中我们一般会使用列表，实际上Python中的列表是链表形式
# 由于List可以存储各种类型的数据而不出错，所以当处理大量数据时，它的占用会很高
# 于是有了Array，即数组，数组作为仅储存单一类型变量的类，占用连续内存，十分利于计算
# 在一般情况下我们体会不到list和array的区别，但是一旦数据内容超过一个阈值，速度区别会很明显
from array import array

# array函数需要首先确定类型，也就是python中叫typecode的东西，中文叫类型码
# 类型码用来告诉array只能存储哪种类型的数据，常用的有'i'->int,'I'->无符号整数,'f'->float,'d'->double
# float称为单浮点，它占用4字节，double称为双浮点，因为它占用8字节，精度更高
numbers = array("i", [1, 2, 3, 4])
numbers.append(5)
print(numbers)
numbers.pop()
print(numbers)
# numbers[0] = 1.1 # 会报TypeError的错误
numbers.insert(3, 5)  # 在索引为3的数前面插入5
print(numbers)
