x = 10 # 默认为十进制表示
print(x) # 10
x = 0b10 # 这是二进制表示，等于十进制的2
print(x) # 直接输出会显示十进制，即2
print(bin(x)) # 输出二进制字符串 '0b10'
x = 0x12c # 这是十六进制表示，等于十进制的300
print(x) # 直接输出会显示十进制，即300
print(hex(x)) # 输出十六进制字符串 '0x12c'

# 在Python中你可以将不同进制的数相加
y = 0b10 + 0x12c
print(y) # 输出相加后的十进制结果

# 对于 a+bi 形式的复数，Python使用j来表示虚部
z = 3 + 4j
print(z) # 输出复数 (3+4j)
print(z.real) # 输出实部 3.0
print(z.imag) # 输出虚部 4.0
