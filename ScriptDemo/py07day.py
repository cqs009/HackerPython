#!/usr/bin/puthon

# =========== I/O =======================

#  ===== 输出 ===========================

hello = 'hi man!'

# 使用print() 函数 输出值
print(hello)


# 使用str() 返回一个用户易懂的字符串表达形式
hello = 1/3
try:
    print(hello + '1212')
except Exception:
    print("数据类型不匹配！")

print(str(hello)+ '1212' )

# 使用 str.format() 函数输出指定格式的值
for i in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(i,i*i,i**i))

# 使用 repr() 返回一个解释器易读的表达形式
hello = 'yes\no'
print(hello)
print('=== 分割线 ===')
print(repr(hello))

# 使用 !a(ascii()),!s(str()),!r(repr()) 在格式化某个值之前对其进行转化





