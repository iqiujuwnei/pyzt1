'''
学习多线程，多线程的实例
'''
# import logging
# import threading
# from time import ctime, sleep
#
# logging.basicConfig(level=logging.INFO)
#
# loops = [2, 4]
# class MyThread(threading.Thread):
#     def __init__(self, func, args, name=''):
#         threading.Thread.__init__(self)
#         self.func = func
#         self.args = args
#         self.name = name
#     def run(self):
#         self.func(*self.args)
# def loop(nloop, nsec):
#     logging.info("start loop" + str(nloop) + "at " + ctime())
#     sleep(nsec)
#     logging.info("end loop" + str(nloop) + "at " + ctime())
#
# def main():
#     logging.info("start all at " + ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         # t = MyThread(loop, loops[i], loop.__name__)
#         t = threading.Thread(target=loop, args=(i, loops[i]))
#         threads.append(t)
#     for k in nloops:
#         threads[k].start()
#     for n in nloops:
#         threads[n].join()
#     logging.info("end all at " + ctime())
#
# if __name__ == '__main__':
#     main()
'''
列表的排序：关键是传如的可变参数，函数直接改变了参数本身。所以可以直接打印参数
'''
# def bidui(list01):
#     for i in range(len(list01)-1):
#         for n in range(i+1, len(list01)):
#             if list01[i] > list01[n]:
#                 list01[i], list01[n] = list01[n], list01[i]
#     # return list01  传入的是可变参数，改变了可变的对象不用return
# list02 = [2,5,1,2,7,9]
# print(bidui(list02))
# print(list02)
'''
位置和关键字
位置传参必须一一对应
关键字参数可以打乱顺序
要注意解压的列表/元祖/字典的值（尤其是元祖是否对应函数的参数名称）
'''
# 实例
# def fun01(a,b):
#     print(a)
#     print(b)
# fun01(1,2)                    #根据位置传参
# fun01(b=1, a=2)               #根据关键子传参
# fun01(*[1, 2])                #解压列表->1，2
# fun01(*(1,2))                 #解压元祖->1，2
# fun01(**{"a": 2, "b": 3})     #解压字典->a=1,b=3
'''
既然有解压传参，那么就应该有压缩参数。第一个压缩元祖
一个函数有且只有一个元组星函数
'''
# def fun02(*args):      #传入的参数最终成为元祖，戏称元祖星函数
#     print(args)
# fun02(1)            #（1，）
# fun02((1, 2))       #((1, 2),)
# fun02({"c": 1})     #({"c": 1},)
# fun02([2, 4])       #([2, 4],)

'''
既然有解压传参，那么就应该有压缩参数。第二个压缩字典
一个函数有且只有一个字典双星函数
'''
# def fun03(**kwargs):      #传入的参数最终成为字典，戏称字典双星函数
#     print(kwargs)
# fun03()            #{}不传值就是空字典
# fun03(a=1, b=2)       #{'a': 1, 'b': 2}
# fun03({"c": 1})     #报错，因为生成的是字典，必须按照字典key和value的方式
'''
单星和参数，元祖星和字典双星

'''
# def fun05(*,p1):
#     print(p1)
# # fun05(1)        #报错
# fun05(p1=2)       #2  和元祖星一样，只是这个时候不再接收元祖参数，后面的参数必须是关键参传参

# def fun06(*args, **kwargs):
#     print(args)
#     print(kwargs)
# fun06()             #() {}  不给参数那么都打印空，双明星类型参数都可以不传
# fun06(1)            #(1, ) {}  传1组成一个元祖，但是没有字典类型答应空
# fun06(a=1)          #() {"a":1}  传a=1,那么元祖打印空，字典打印

'''
元祖星和双星几位置参数，默认参数组合传参的方式
主要强调：第一位可以位置可以关键字，元祖星后面参数必须用关键字。默认参数可传可不传，字典双星也是可传可不传。
元祖单星在最后也是可传可不传
'''
# def fun04(a, *args, b, c="cc", **kwargs):
#     print(a)
#     print(args)
#     print(b)
#     print(c)
#     print(kwargs)
# fun04(1, 2, b=3)                #a按照位置，args按照位置，但是args后面参数必须按照关键字，所以b=3，默认参数可以不传，字典双星可以不传
# fun04(a=1, 2, b=3, c="CC")      #a按照关键字，args按照位置，但是args后面参数必须按照关键字，所以b=3，默认参数更改为大C，字典双星可以不传
# fun04(1, 2, b=3, c="CC", f=5)   #多了一个f=5是传给字典双星。


'''
python 实战一作业
'''


# name = 'xiaoming'
# 1、无return 返回None，只是return也返回None
# 2、方法中参数没有默认值，调用的必须传值。
def func(name):
    print(name)  # 打印xiaoming
    return  # 返回None


print(func('xiaoming'))


# 3、return 后的返回值可以是变量，调用后返回对应变量值
# 4、方法中参数有默认值，调用时不传值。打印和返回都是默认值
def func(name='xiaoming'):
    print(name)  # 打印xiaoming
    return name  # 返回小明


print(func())


# 5、return 后返回值也可以是具体的值数字字符串等。调用后返回给定的值
# 6、方法中参数有默认值，调用的时候传值，打印传的值和返回固定值
def func(name='xiaoming'):
    print(name)  # 打印xiaoxin
    return 'lisi'  # 返回lisi


print(func(name='xiaoxin'))

'''
python 实战二作业
'''

import yaml


class Animal:
    def __init__(self, name, color, gender, age):
        self.name = name
        self.color = color
        self.gender = gender
        self.age = age

    def cry(self):
        return "会叫"

    def run(self):
        return "会跑"


class Cat(Animal):
    def __init__(self, name, color, gender, age, hair="短毛"):
        super().__init__(name, color, gender, age)
        self.hair = hair

    def Catch_mouse(self):
        return "会抓老鼠"

    def cry(self):
        return "会喵喵叫"


class Dog(Animal):
    def __init__(self, name, color, gender, age, hair="长毛"):
        super().__init__(name, color, gender, age)
        self.hair = hair

    def Watch_the_house(self):
        return "会看家"

    def cry(self):
        return "会汪汪叫"


if __name__ == '__main__':
    with open("ztte.yml", "rb") as f:
        # a = yaml.load(f, Loader=yaml.FullLoader)
        a = yaml.safe_load(f)
        cat = a['cat']
        dog = a['dog']

cat01 = Cat(cat['name'], cat['color'], cat['gender'], cat['age'])
print(f"小猫的名字叫{cat01.name}，周身{cat01.color}色{cat01.hair}，已经{cat01.age}的小{cat01.gender}猫,{cat01.Catch_mouse()}")

dog01 = Dog(dog['name'], dog['color'], dog['gender'], dog['age'])
print(f"毛孩子名字叫{dog01.name}，浑身{dog01.color}{dog01.hair},刚刚{dog01.age}的小{dog01.gender}狗,{dog01.Watch_the_house()}")
