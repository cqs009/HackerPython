#!/usr/bin/python
'''
    testpage包下的模块
'''


def test():
    '''
        模块函数 test()
    '''
    return 'hello 亡命之徒'

def summation(num1=0,num2=0):
    '''
        自定义求和函数
    '''
    return num1 + num2

def quadrature(num1=0, num2=0):
    '''
        自定义求积函数
    '''
    return num1 * num2

def differencing(num1=0, num2=0):
    '''
        自定义求差函数
    '''
    return num1 - num2

def division(num1=0, num2=0):
    '''
        自定义求商函数
    '''
    if(num2 == 0):
        return 0
    return num1 / num2