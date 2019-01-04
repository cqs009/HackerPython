#!/usr/bin/python


class Animal:
    ''' 动物类 '''

    # 动物类型
    animaltype = ''

    #动物特征
    feature = ''

    def __init__(self,animaltype,feature):
        self.animaltype = animaltype
        self.feature = feature
        print('初始化动物类')

    def tell(self):
        ''' 细节 '''
        print('这是: %s 动物，特征是: %s ' %(self.animaltype,self.feature))


    
# 一个继承了动物类得老虎类

class Tiger(Animal):

    # 老虎名称
    tigername = ''
    # 老虎年龄
    age = 0
    # 老虎性别
    sex = ''
    # 老虎种类
    tigertype = ''

    ''' 这是一个老虎的类 '''
    def __init__(self,tigername,age,sex,tigertype):
        ''' 这是一个构造函数 '''
        self.tigername = tigername
        self.age = age
        self.sex = sex
        self.tigertype = tigertype
        print("初始化老虎类")
    
    def tell(self):
        print("名称：%s \n年龄：%d\n性别：%s\n种类：%s" %(self.tigername,self.age,self.sex,self.tigertype))

    def run(self):
        print("%s 在奔跑" %(self.tigername))

class Chicken(Animal):

    # 颜色
    chickencolor = ''

    # 类别
    chickentype = ''

    # 食物
    food = ''

    def __init__(self,chickencolor,chickentype,food):
        Animal.__init__(self,'禽类','卵生，有毛')
        self.chickencolor = chickencolor
        self.chickentype = chickentype
        self.food = food

    def eat(self):
        print('这个 %s 色的 %s 鸡,正在吃 %s' %(self.chickencolor,self.chickentype,self.food))


t = Tiger('脑斧',3,'雄性','华南虎')

t.tell()

c = Chicken('黄','野生','老虎')

c.eat()





