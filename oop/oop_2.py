#coding:utf-8

# class Person(object):
#     def __init__(self,name,wage):
#         self.name = name
#         self.wage = wage
#
#     def func(self):
#         return '123'
#
#     @property #方法变为属性
#     def attr(self):
#         return '123'
#
#     def computer(self):
#         return '555'
#
# #类成员字段 （字段，方法，属性）
#
# obj = Person('jack',20000)
# print(obj.func())
# print(obj.attr)

# class Province(object):
#     #静态字段
#     country = "中国"
#
#     def __init__(self,name):
#         self.name = name
#
# shanxi = Province("山西")
# print(id(shanxi.country))
# shandong = Province("山东")
# print(id(shandong.country))
# henan = Province("河南")
# print(id(henan.country))

#类成员：方法

# class Province(object):
#     def __init__(self,name):
#         pass
#
#     def f1(self): #普通方法
#         pass
#
#     @classmethod #类方法
#     def f2(cls):
#         print("i am f2")
#         print(cls)
#
#     @staticmethod #静态方法
#     def f3(s1,a1):
#         print("%s is reading %s"%(s1,a1))
#
# # obj = Province()
# # obj.f1()
#
# Province.f2() #调用都用类
# Province.f3('tony',"book")

#类成员：属性

# class Goods:
#     @property
#     def price(self):
#         return "wupeiqi"
#
# g = Goods()
# print(g.price)

# class Pager:
#
#     def __init__(self,current_page):
#         self.current_page = current_page
#         self.per_items = 10
#
#     @property
#     def start(self):
#         val = (self.current_page - 1)*self.per_items + 1
#         return val
#
#     @property
#     def end(self):
#         val = self.current_page * self.per_items
#         return val
#
# p = Pager(1)
#
# print(p.start)
# print(p.end)

class Foo:
    def get_bar(self):
        return 'wupeiqi'

    BAR = property(get_bar)

obj = Foo()
result = obj.BAR
print result















