# #注释 erdian
#
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

# name = 'xiaoming'
# 1、无return 返回None，只是return也返回None
# 2、方法中参数没有默认值，调用的必须传值。
def func(name):
    print(name)  #打印xiaoming
    return       #返回None
print(func('xiaoming'))

# 3、return 后的返回值可以是变量，调用后返回对应变量值
# 4、方法中参数有默认值，调用时不传值。打印和返回都是默认值
def func(name='xiaoming'):
    print(name)  #打印xiaoming
    return name  #返回小明
print(func())

# 5、return 后返回值也可以是具体的值数字字符串等。调用后返回给定的值
# 6、方法中参数有默认值，调用的时候传值，打印传的值和返回固定值
def func(name='xiaoming'):
    print(name)     #打印xiaoxin
    return 'lisi'    #返回lisi
print(func(name='xiaoxin'))