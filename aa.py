import random
from itertools import count
from sys import prefix

if __name__ == '__main__':
    # day = 4
    # match day:
    #     case 1:
    #         print("11")
    #     case 2:
    #         print("22")
    #     case _:
    #         pass
    #
    # a = 10
    # while a > 0:
    #     print(f"你好{a}")
    #     a -=1
    # else:
    #     print("循环结束")
    #
    #
    #
    # for i in 'assbd':
    #     print(i)
    # else:
    #     print("处理结束")
    #
    #
    # for i in range(10):
    #     for j in range(10):
    #         print("*", end=" ")
    #     print()
    #
    # for i in range(1, 10):
    #     for j in range(1, i + 1):
    #         print(f"{j} * {i} = ", (i) * (j), sep="", end="  ")
    #     print()
    # for i in range(1, 10):
    #     print(i)
    #
    # help(range)

    # import random
    #
    # a  =random.randint(1, 10)
    # help(random)
    # print(a)

    # a = [1,2,3,5,2,3423,13]
    # help(a)
    # for i in a:
    #     print(i)
    # help(list)
    # 正向索引
    # print(a[0])
    # # 列表可以从后向前遍历   最后的那个下标为 -1 从-1开始
    # print(a[-1])
    # print(a[-2])
    # 元素的修改
    # a[1] = True
    # print(a[1])
    # 删除指定位置的元素
    # del a[0]
    # print(a)

    # 集合切片获取
    # print(a[0:5:2])
    # print(a[:5])
    # print(a[-1:-5])
    # # 切片索引可以混用
    # print(a[0:-1])

    # 排序桉树
    # a.sort()
    # print(a)
    # a.reverse()
    # print(a)
    # def aa(b):
    #     return b >0;
    #
    # a.sort(key=abs)
    # print(a)
    # print(sum(a))

    # 判读那元素是否在列表中
    # if 12 in a:
    #     print("asd")
    # else:
    #     print("不存在")

    # 解包，将容器这种东西解开为一个个独立的元素 就是用 * 来解包 可以用来合并列表
    # b = [*a]
    # print(b)
    # b = a + a
    # print(b)

    # a = [1,2,3,5,2,3423,13]

    # 这是列表推导式的形式  [表达式 for i in range(1, 11)] 列表元素的值就是这个表达式的值
    # b = [str(i * 12) for i in range(1, 11)]
    # print(b)
    # b = [ random.randint(1, 20) for i in range(1, 21)]
    # print(b)
    # # 带条件的列表推导式
    # c = [i**2 for i in b if i % 2 == 0]
    # print(c)

    # a = 'weqQasda'
    # help(str)
    # print(a.lower())
    # print(b)
    # print(a.join(b))
    # 字符串正向索引
    # print(a[0])
    # 反向索引
    # print(a[-1])
    # a[1] = 's'
    # 字符串切片  和列表一样
    # print(a[0:3])
    # print(a[:3:2])
    # 中间不写 意味末尾
    # print(a[0::1])
    # 反向切片
    # print(a[-1:-4:-1])
    # print(a[::-1])
    # help(str)
    # a = 'weqQasdaQa '
    # print(a.find('Qa'))
    # print(a.count('Qa'))
    # print(a.strip())
    # print(a.split('s'))
    # help(str)
    # # a.replace()
    # print(a.replace('Qa', 'gg', 1))
    # print(a.startswith('we'))


    # 元组
    # 元组的元素不可修改，只能查询

    # t = (2, 3, 1 ,5, 23, 1,'2')
    # print(t)
    # print(t[1])
    # print(t[1:4:2])
    # # 定义一个空元组
    # # a = tuple()
    # # print(a)
    # # help(tuple)
    # print(t.count(1))
    # # 元组不可以修改
    # # t[1] = 2
    # # index 第一个元素出现的索引位置
    # print(t.index(1))
    #
    # # 只有一个元素的不是元组，因为元组不可变，这和t2 = 100完全一样。
    # t2 = (100)
    # print(type(t2))
    #
    # t3 = (3, 4)
    # # 元组的解包  这是基础解包
    # a,b = t3
    # print(a, b)
    # t = (2, 3, 1, 5, 23, 1, '2')
    # # 这是元组的扩展解包， 用*来收集剩余的元素 放到一个列表里面
    # x, *y, z = t
    # print(x)  #2
    # print(y)  #[3, 1, 5, 23, 1]
    # print(z)  #2
    # a = 10
    # b = 20
    # # t = (a, b)
    # # b, a其实是个元组，元组也可以不写外面的括号的,这里是组包和解包的操作
    # a, b = b, a
    # print(a)
    # print(b)
    # a = 100
    # b = 200
    # c = 300
    # # abc  -》 cab
    # c,a,b = a,b,c
    # print(c, a, b)

    # stu = (
    #     ("S001", "王林", 85, 92, 78),
    #     ("S002", "李慕婉", 92, 88, 95),
    #     ("S003", "十三", 78, 85, 82),
    #     ("S004", "曾牛", 88, 79, 91),
    #     ("S005", "周轶", 95, 96, 89),
    #     ("S006", "王卓", 76, 82, 77),
    #     ("S007", "红蝶", 89, 91, 94),
    #     ("S008", "徐立国", 75, 69, 82),
    #     ("S009", "许木", 86, 89, 98),
    #     ("S010", "通天", 66, 59, 72)
    # )
    #
    # # for s in stu:
    # #     total = s[2] + s[3] + s[4]
    # #     name = s[1]
    # #     av = total / 3
    # #     print(f'{name}:总分:{total},平均分:{av}')
    #
    # # 直接解包式写法
    # for id,name,yuwen,shuxue,yingyu in stu:
    #     print(id,name,yuwen,shuxue,yingyu)

    # 集合 Set
    # 特点不会重复这是区别于列表和元组的根本特点，也是使用时考虑的重点，也是无序的，可修改 就是java的Set
    # s = {1,2,43,6,2,1} #会自动去重
    # # print(s)
    # # help(set)
    # # a = set('121adsssd')
    # # print(a)
    # # s.add('t')
    # # print(s)
    # # # 定义空集合 不能适应{}定义 这是字典
    # # v = set()
    # # 删除集合元素
    # # s.remove(1)
    # # print(s)
    # s.pop()
    # print(s)

    # ------------------------ 集合 set 案例 ------------------------

    # # 选修足球的学生名单
    # football_set = {"王林", "曾牛", "徐立国", "通天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
    #
    # # 选修篮球的学生名单
    # basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
    #
    # # 选修法语的学生名单
    # french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
    #
    # # 选修艺术的学生名单
    # art_set = {"遥天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
    #
    # # 1. 找出同时选修了法语和艺术的学生
    # print(french_set.intersection(art_set))
    # print(french_set & art_set) #这种也可以求交集
    #
    # # 2. 找出同时选修了所有四门课程的学生
    # print(football_set.intersection(basketball_set).intersection(french_set).intersection(art_set))
    # print(football_set & basketball_set & french_set & art_set)
    # # 3. 找出选修了足球，但是没有选修篮球的学生
    # print(football_set.difference(basketball_set))
    # print(football_set - basketball_set)
    # print({i for i in football_set if i not in basketball_set})
    # # 4. 统计每一个学生选修的课程数量
    # # print(football_set.union(basketball_set).union(french_set).union(art_set))
    # # for name in football_set.union(basketball_set).union(french_set).union(art_set):
    # # for name in football_set | basketball_set| french_set| art_set:
    # #     total = 0
    # #     if name in football_set:
    # #         total+=1
    # #     if name in basketball_set:
    # #         total+=1
    # #     if name in french_set:
    # #         total+=1
    # #     if name in art_set:
    # #         total+=1
    # #     print(f"学生:{name},选课总数:{total}")
    #
    # allset = football_set | basketball_set | french_set | art_set
    # alllist = [* football_set, * basketball_set, * french_set, * art_set]
    # for e in allset:
    #     total = alllist.count(e)
    #     print(f"学生:{e},选课总数:{total}")

    # help(set)

    # 字典学习
    # 其实就是java的Map     key必须是不可变类型
    # 定义字典
    # dict()空字典
    # d = {'a':12,'b':34}
    # print(d)
    # # help(dict)
    # # 两种获取值的方式
    # print(d['a'])
    # print(d.get('a'))
    # # 已存在就是修改  不存在就是添加
    # d['a'] = 45
    # d['c'] = 46
    # # print(d)
    # # # 弹出键值  同时也是删除了
    # # d.pop('a')
    # # print(d)
    # # # 也可以删除key
    # # del d['c']
    # # print(d)
    # print(d.keys())
    # # for key in d.keys():
    # #     print(type(key))
    #
    # print(d.values())
    #
    # # 返回所有的键值对
    # print(d.items())
    # for item in d.items():
    #     # item是一个元组
    #     print(item[0], item[1])
    # num = 100
    # def hah():
    #     """
    #     这是我的函数
    #     :return:
    #     """
    #     # 这是局部变量
    #     # num = 10000
    #     # print(num)
    #     # 以全局变量的权限去使用这个num
    #     global num   #先定义全局
    #     num = 10000  #再使用
    #     print(num)
    #     return '11'
    #
    # # help(hah)
    # # print(hah())
    # hah()
    # print("----")
    # print("num:", num)

    # 函数
    # def aa(a,b='b',c='c'):
    #     print(f"{a},{b},{c}")
    #
    # aa(a='d',c='c')

    # *args位置不定长参数
    # def aa(*args):
    #     print("asd", args)
    #
    # aa(1,2,3)

    # 基于关键字的不定长参数  会将参数封装为一个字典
    # def aa(** kwargs):
    #     print("", kwargs)
    #
    # aa(a='v', v='asd')

    # def a(x, y, b):
    #     print(b(x,y))
    # def b(x, y):
    #     return x + y
    #
    # # lambda 参数列表:函数体
    # a(1, 2, lambda x,y:x+y)

    # 用变量接受匿名函数
    # ad = lambda x,y: print(x+y)
    # print(ad(1, 2))

    # 无参的匿名函数
    # a = lambda : print("------")
    # a()
    # a = ['C','asd4','asd2234242','ert51']
    # a.sort()
    # print(a)
    # a.sort(key=lambda x:len(x))
    # print(a)
    # def jiecheng(a):
    #     if a == 1:
    #         return 1
    #     res = a * jiecheng(a-1)
    #     return res
    #
    #
    # print(jiecheng(8))

    # 类型注解 感觉用处不大
    # a: int = 12
    # b: float = 1.2
    # print(a, b)
    # names: list[str|int] = ['1',2]
    # print(names)
    # c: bool = True
    # print(c)
    # d: dict[str, int] = {'a':12}
    # print(d)
    # # 一个元素的元组就是一个字符串  如果用元组的形式写 必须加一个逗号
    # e: tuple[str] = ("a",)
    # print(e)
    # 函数注解类型   b: list[int] 参数的类型  -> list[int]  返回值的类型
    # def aa(b: list[int]) -> list[int] :
    #     print(b)
    #     return b
    # aa([1,2, '3'])
    # import bb
    # # import os
    # import random
    #
    # print(random.randint(1, 10))
    # print(bb.add(1, 2))
    # from random import randint
    #
    # print(randint(1, 20))
    # 这种写法 bb这个模块不会被导入的，只会导入bb中__all__ 里面配置的所有内容
    # from bb import *
    #
    # print(add(1, 2))
    # import util.my
    #
    # print(util.my.add(1, 24))
    # from util.my import add

    # print(add(1, 4))
    # from util import *
    #
    # print(my.add(1, 2))
    # myFunc.jianshu()
    #
    # from util.my import add
    #
    # print(add(1, 2))



    # 类与对象

    # class A:
    #     pass
    #
    # a = A()
    # # 动态的添加属性  为对象增加属性  这和java不一样
    # a.name='qwx'
    # # __dict__这个默认的属性 存储的是对象中所有的属性值
    # print(a.__dict__)


    # from bb import *
    # a = A(4,56, 'weiz')
    # # print(a.__dict__)
    # # a.run(3,4)
    # # # 比如说这里直接打印这个a  那么python会自动调用__str__的魔法方法  这就类似于java的toString()方法 但java一定会显示的调用的
    # # print(a)
    # # a1 = A(3,56)
    # # print(a == a1)
    # # print(a <= a1)
    # # print(a >= a1)
    # #
    # # print(a.name)
    # # print(a1.name)
    # # print(A.name)
    # # 这里的name  如果示例属性和类属性都有  这里展示的就是示例属性
    # print(a.name)
    # print(A.name)

    # 异常
    # try:
    #     a = 1 / 0
    #     # print(ad)
    # except Exception as e:
    #     print("yichang", e)
    # finally:
    #     print('最周')
    # import util as ut
    #
    # print(ut.titleaa)
    # ut.my.add(1, 2)

    from util import jiajia

    jiajia()