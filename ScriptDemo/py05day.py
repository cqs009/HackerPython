#!/usr/bin/ypthon
# ==================== 模块 ===========================
import sys

print('命令参数如下：')

for item in sys.argv:
    print(item)

print('\npython的路径：', sys.path,'\n')

# import:模块导入指令
# sys.py:这个模块是python标准库的

#=======================================================
# ============= module1.py作为模块，并调用其中的函数===============


import module1 

print(module1.hello())

# ======== 将模块得内容导入到当前得命名空间中，*号就是表示所有 ====
from module2 import *

print(quadrature(2,5))

# __name__属性：每个模块都有得一个属性，当值为__main__时，表明该模块自身在运行，否则就是被引入得
if __name__ == '__main__':
    print('这是我自己')
else:
    print('这是其他模块')

# dir() 得到当前模块中定义得属性列表
print(dir())

# ==========================================================================

# ============ 包的使用 ================================
from testpage import testmodule

print (testmodule.test())

print(testmodule.division(2))

