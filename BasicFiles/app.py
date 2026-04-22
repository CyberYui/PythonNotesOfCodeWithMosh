mystr = "    Hello, World!    "
print("mystr:", mystr)  # 输出原字符串，包含两端的空格
print("mystr.find('World'):", mystr.find("World"))  # 输出 "World" 在字符串中的索引
print("type(mystr):", type(mystr))  # 输出字符串的类型
newstr = mystr.format()  # 字符串的 format 方法，返回一个新的字符串
print("newstr:", newstr)  # 输出使用 format 方法返回的新字符串
print(
    "mystr == newstr:", mystr == newstr
)  # 输出比较结果，说明 mystr 和 newstr 是相同的字符串对象

print(mystr.capitalize())  # 将字符串的第一个字符转换为大写，其他字符转换为小写
print(mystr.strip())  # 删除字符串两端的空格
