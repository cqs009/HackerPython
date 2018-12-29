#!/usr/bin/python
# ================================== python 异常和错误 ==================================

# 错误：编译时语法的错误 

#while True
#   print('hello world')

# 异常：运行时检测到的错误
# print(1/0)

# =======================================================================
# ================== 异常处理 ============================================

# try/except语句：
# 工作方式：
#       先执行try和except之间的代码块包括函数，如果没有异常则忽略except下的代码块
#       如果有异常则进入except执行except下的代码块；异常代码后面的代码不执行
#       一个try语句可以有多个except子语句，也可用括号将多个异常组成组元

# =========================================================================
# 实例 1
try:
    print(1/0)
except ZeroDivisionError :
    print('这个是一个运行时异常 0不可以被作为除数')
# =======================================================================
# 实例 2

try:
    print(x/0)
except ZeroDivisionError :
    print('这个是一个运行时异常 0不可以被作为除数')

except NameError :
    print('这个是一个运行时异常 找不到这个变量啦')

# ======================================================================
# 实例 3
try:
    print(x/0)
except (ZeroDivisionError, NameError, ValueError):
    print('这个是一个运行时异常')

# ===========================================================================

# try/except/else 语句 else子语句表示在没有发生任何异常时执行
from testpage import testmodule
try:
    print(testmodule.differencing())
except (ZeroDivisionError, NameError, ValueError):
    print('这里有异常')
else:
    print('没毛病啊')

# ============================================================================

# 使用 raise 抛出异常
#try:
#   raise NameError('异常从这里抛出')
#except NameError:
#    print("这个是NameError异常")
#    raise

# ============================================================================

# 自定义异常
class MyError(Exception):
    '''
        自定义的异常类
    '''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(1*2)
except MyError as e:
    print('我的自定义异常', e.value)
    
# =============================================================================

# 自定义异常基础类
class BaseError(Exception):
    ''' 异常处理的基础类 '''
    pass

class InputError(BaseError):
    ''' 抛出一个输入错误的异常 

            属性：
            expression -- 发生错误时输入的参数
            message    -- 异常信息

    '''
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

# ================================================================================

# finally 语句： 无论是否发生异常都进入执行代码

def divide():

    try:
        x = input("请输入被除数：")
        y = input("请输入除数：")

        result = int(x) / int(y)
    except ZeroDivisionError:
        print("除数位0")
    else:
        print("商：",result)
    finally:
        print("谁也不能阻止我输出")

divide()