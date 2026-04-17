# 与栈相反的是队列，它是一种先进先出(FIFO)的结构
# 可以看成类似于现实生活中等待进入餐厅的队伍，先来后到
# 当然也可以使用列表来模拟队列，但是要知道，如果一个队列十分长
# 那么如果移动列表元素，效率会很低，比如移除第一个元素，那么后面的其余元素都要向前移动一位
# 因此，使用collections.deque对象来实现队列效率更高
from collections import deque

# collections是Python中内置的高级数据结构库，相比于普通的list，dictionary，tuple，它更加实用
# deque正是其中常用的一个数据结构：双端队列(double-ended queue)，它支持从两头进行增删
# 可以简单地理解其为超级加强版 list，两头增删都超快
# 事实上deque是一个类，它和list有一些同名的函数可以调用，也使得我们能像使用list一样使用它
queue = deque([])
# 使用append函数会向队尾添加元素，append函数是deque类中的一个函数
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.append(7)
queue.append(8)
print(queue)
# 如果需要在队列开始移除一个元素，使用popleft函数即可
queue.popleft()
print(queue)
# 如果要在队尾移除一个元素，使用pop函数，请注意这里的pop函数并不是list的那个，只是同名
queue.pop()
print(queue)
# 如果要在队列开始添加一个元素，使用appendleft函数即可
queue.appendleft(1)
print(queue)
