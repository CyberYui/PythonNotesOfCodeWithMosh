# 在python中，条件语句用于根据条件执行不同的代码块。它允许程序根据不同的条件执行不同的操作。
age = 22
# Python中和其他语言类似，条件计算符为：==、!=、>、<、>=、<= 
if age >= 18:
    print("You are eligible to vote.")
elif age >= 13:
    print("You are a teenager, not eligible to vote.")
else:
    print("You are a child, not eligible to vote.")

print("all done!")

# 在python中，也是有逻辑运算符的，可以是and、or、not
name = "CyberKaka"
age = 12
if not name.strip():
    print("Name is empty.")
    # Python中可以连接条件运算符，下面的if语句可以写为if 18 <= age < 65:
elif age >= 18 and age < 65:
    print("Eligible")
elif age >= 65:
    print("Senior")
elif 13<=age<18:
    print("Teenager")
else:
    print("Child")
print("Done!")

# 在Python中也有三元运算符，语法为：value_if_true if condition else value_if_false
# 在Java等其他编程语言中，三元运算符的语法为：condition ? value_if_true : value_if_false
name = "CyberKaka"
age = 12
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
# 显然Python的三元运算符比Java的更简洁，更易读，且更符合逻辑
