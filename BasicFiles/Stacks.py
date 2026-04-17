# Stack指栈，是一种后进先出的LIFO(Last-in First-out)结构
# 可以将其想象成一个有层次的物体的堆叠，最上面的物体最先被移除
# 但是实际上Python中并没有专门的栈对象，通常以列表来进行模拟栈
# 借用append()和pop()方法来模拟栈的入栈和出栈操作
browssing_session = []
browssing_session.append(1)
browssing_session.append(2)
browssing_session.append(3)
print(browssing_session)
last = browssing_session.pop()
print(last)
print(browssing_session)
# 现在我们可以通过pop函数推出栈顶元素，通过[-1]索引查看栈顶元素
# 那么我们就可以通过检测是否有栈顶值来判断栈是否为空
if not browssing_session:
    # 如果列表为空，则判断为True，输出"empty"
    print("empty")
else:
    # 如果列表不为空，则判断为False，输出"redirect"，并查看栈顶元素，即最后入栈的元素
    print("Top is:", browssing_session[-1])
