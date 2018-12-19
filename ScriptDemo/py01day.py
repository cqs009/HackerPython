#!/usr/bin/python

# -*- coding:utf-8 -*-
 
a = 0xFF
print("a = "+str(a))

b = 0o10
print("b = "+ str(b))

c = 2462436147273461413471363147171437
print("c = "+str(c))

print(bool(None))
print(bool(1))

print(bool(0))

print(bool(0.00))

print(bool(True))

print(bool(False))

print(bool("true"))

print(bool(''))

print(bool('false'))

print(bool([]))

print(bool((1,)))

# ==================关于 布尔值 bool() 总结 ==========================;
# 特性：整型的子类型，布尔型数据只取 True和False，分别对应整型的 1和0;
# 测试可知以下场景的布尔值为 False,其他为 True。它们分别是：
#       None; 0 (整形); Flae(布尔型); 0.0(浮点型); 0.0+0.0j(复数);
#       ''/""(空字符); [](空列表); ()(空元组); {}(空字典/空集合);
# ===================================================================;
print('========分割线==========')
foo = 2333
bar = foo < 2333

print(bar)
print(bar + foo)

print("%s" %bar)

print("%d" %bar)



