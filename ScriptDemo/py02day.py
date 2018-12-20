#!/usr/bin/python

# ============================== 字符数据类型 =======================================

# 字符串 常用的数据类型，使用 ' 或 " 进行创建

str1 = "hello world!!"
str2 = '食屎啦嘞'

print(str1)
print(str2)

# 字符串截取

print(str1[1:3])

print(str2[-1])



# 字符转义使用反斜杠（\）

print('\a')
print ('hello\000world')

# 字符串运算

namestr = '亡命之徒'

statusstr= "单身狗"
# 字符链接
print(statusstr + namestr)

# 重复输出
print(statusstr * 2)

# 判断字符串是否包含某个特定字符 
print('狗' in statusstr)
print('亡' not in statusstr)

# 将所有字符串按照字面意思来使用，没有转义特殊或不能打印的字符
print('yes\no')
print(r"yes\no")

# 格式化字符串
print("我是 %s 也叫 %s" %(namestr, statusstr))

# 三引号

helpstr = """
        IS: python [OPTIONS]
            -h          Display this IS message
            -t          exit
            """
print(helpstr)
#============================================ 分割线 =============================================

# ============================================ 数据结构 ==========================================

#============================= List 列表 =========================================================

list1 = ['白切鸡', '芹菜肉丝', '土豆炒肉', '梅菜扣肉', '小炒鱼', '烤羊排']
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = ['F', "e", "d", 'c', 'b', 'a', 9, 8, 7, 6]

# 访问列表 使用 [] 和下标索引来访问列表里的值
print(list1[3])

# len() 该函数返回指定参数的长度

print(len(list2))




