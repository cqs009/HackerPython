#!/usr/bin/python

# ======================== 函数 ===========================

# 函数定义格式： def 函数名(参数列表)
#                   函数体
# =========================================================

def hello():
    '''这个是一个函数的实例.
    '''


    print('hello world')


hello()
# ==================================================================
# 默认参数值

def defaultParam(param1,param2 =1):
    '''
        默认参数测试函数1
    '''
    return param1 * param2


print(defaultParam('aaa'))

print(defaultParam('hello',5))
# ==================================================================
# 关键字传参

def func1(p1,p2=2):
    '''
        关键字传参设置
    '''
    print('p1=',p1,'p2=',p2)

func1(10,p2=999)

# =============================================================
# 查看函数说明
print(defaultParam.__doc__)
help(hello)

#====================== 作业1.1=======================================
username = ''
pwd = ''

def login():
    '''
        用户登录函数
    '''
    username = input('用户名：')
    if username == 'seven':
        checkpassword()
    else:
        print('您输入得用户名无效，请重新输入')
        login()


def checkpassword():
    '''
        密码校验函数
    '''

    pwd = input('密码：')
    if pwd == '123':
        print('登录成功！')
    else:
        print('密码错误！，请重新输入')
        checkpassword()


login()
# ==================== 作业2.2 ========================================

def algorithmForPeace(starnum=2,lens=100):
    '''
        自定义求和函数
    '''
    num = starnum
    count = 0
    while(num <= lens):
        if (num%2) == 0:
            count = count + num
        else:
            count = count - num
        num = num + 1

    return count

print(algorithmForPeace())

