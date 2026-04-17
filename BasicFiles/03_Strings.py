course = "Python Programming for Beginners"
print(len(course))
print(course[0]) # 输出字符串的第一个字符
print(course[-1]) # 输出字符串的最后一个字符
print(course[0:6]) # 输出字符串的前6个字符,不包括第6个字符
print(course[0:]) # 输出字符串的所有字符
print(course[:6]) # 输出字符串的前6个字符,不包括第6个字符
print(course[:]) # 输出字符串的所有字符
print(course[1:]) # 输出字符串的第2个字符到最后一个字符
print(course[1:10:2]) # 输出字符串的第2个字符到第10个字符,步长为2
print(course[::2]) # 输出字符串的所有字符,步长为2
print(course[1::2]) # 输出字符串的第2个字符到最后一个字符,步长为2
print(course[1:10:3]) # 输出字符串的第2个字符到第10个字符,步长为3

# Python允许字符串进行连接和重复
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name) # 输出连接后的字符串
# 我们也可以使用f-string来连接字符串
full_name_fstring = f"{first_name} {last_name}"
print(full_name_fstring) # 输出连接后的字符串
# f的大小写不影响结果
full_name_fstring_upper = F"{first_name} {last_name}"
print(full_name_fstring_upper) # 输出连接后的字符串
# f-string还支持表达式，在{}中可以放入任何有效的Python表达式，甚至可以添加反义运算符
full = f"{first_name} {last_name} is {len(full_name)} characters long, there are {1 + 1} words in \"full\""
print(full) # 输出包含表达式的字符串

# 接下来可以看一些有用的字符函数
print(full_name.upper()) # 输出大写的字符串
print(full_name.lower()) # 输出小写的字符串
print(full_name.title()) # 输出首字母大写的字符串
print(full_name.capitalize()) # 输出首字母大写的字符串
print(full_name.strip()) # 输出去除两端空格的字符串
print(full_name.lstrip()) # 输出去除左侧空格的字符串
print(full_name.rstrip()) # 输出去除右侧空格的字符串
print(full_name.find("John")) # 输出子字符串在原字符串中的位置
print(full_name.replace("John", "Jane")) # 替换字符串中的子字符串
print("John" in full_name) # 检查子字符串是否在原字符串中
print("Jane" not in full_name) # 检查子字符串是否不在原字符串中
