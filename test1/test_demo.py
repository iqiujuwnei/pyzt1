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
import pytest
class Testcalls01:

    @pytest.mark.dependency(name="a01")
    def test_a01(self):
        pass
    @pytest.mark.dependency(depends=["a01"])
    def test_a02(self):
        pass

class TestClass(object):

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["TestClass::test_b"])
    def test_d(self):
        pass
    @pytest.mark.run(order=1)
    @pytest.mark.dependency()
    def test_b(self):
        pass



class TestClassNamed(object):

    @pytest.mark.dependency(name="a")
    @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency(name="b")
    def test_b(self):
        pass

    @pytest.mark.dependency(name="c", depends=["a"])
    def test_c(self):
        pass

    @pytest.mark.dependency(name="d", depends=["b"])
    def test_d(self):
        pass

    @pytest.mark.dependency(name="e", depends=["b", "c"])
    def test_e(self):
        pass


if __name__ == '__main__':
    pytest.main()