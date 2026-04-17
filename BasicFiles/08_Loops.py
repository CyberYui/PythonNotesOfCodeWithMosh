"""
This doc includs some loop exercises
"""
# 同其他程序语言动辄三四种循环语句不同，在Python中，只有两种循环语句：for和while
# for循环
for number in range(0,10,2):
    print(number)
# 这样会循环输出4个数字，0，1，2，3
# 但是range函数返回的并不是一个列表，它不会一次性生成所有数字，而是用一个生成一个
print(type(range(1))) # <class 'range'>
# range函数一般会有下面三种使用方式
# range(5)        # 一个参数，代表直接输出几个数，5就代表0~4
# range(2,6)      # 两个参数，代表从2开始到6结束，但是不包括6，也就是2，3，4，5这4个数
# range(1,10,2)   # 三个参数代表从1开始到10结束，步长为2，即从1到10的所有奇数
# range(0,10,2)   # 三个参数代表从0开始到10结束，步长为2，即从0到10的所有偶数,但是不包括10
# for循环还有个for-else的用法，当for循环正常结束（没有break）时，会执行else语句，否则不会执行
for number in range(0,10,2):
    print(number)
    break
else:
    print("循环结束")

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for nami in names:
    # startswith函数判断字符串是否以某个字符开头
    if nami.startswith("B"):
        print("Found")
        break
else:
    print("Not Found")

# while循环
# while循环和for循环一样，也有while-else的用法
count = 0
while count < 10:
    print(count)
    count += 1
    break
else:
    print("循环结束")
# while循环还有一个continue的用法，当遇到continue时，会跳过本次循环，直接进入下一次循环
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
# while循环同样有break的用法，当遇到break时，会直接跳出循环
guess = 0
answer = 5
while answer != guess:
    guess = int(input("Guess a number: "))
    if guess == answer:
        print("You got it!")
        break
    elif guess < answer:
        print("Too low")
    else:
        print("Too high")
# 当我们不想使用break跳出循环时，可以使用一个Flag来控制循环的结束，比如这里的answer
guess = 0
while answer != guess:
    guess = int(input("Guess: "))
    