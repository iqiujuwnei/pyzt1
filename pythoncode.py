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