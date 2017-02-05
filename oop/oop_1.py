#coding:utf-8

#方式一 函数式编程
# def fetch():
#     pass
#
# def modify():
#     pass
#
# def remove():
#     pass
#
# def create(arg):
#     #连接数据库，hostname,port,username,password,db
#     #打开数据库
#     #添加数据
#     #关闭
#     pass

#方式二 面向对象封装

# class Foo:
#
#     def __init__(self,hostname,port,username,password,db):
#         self.hostname = hostname
#         self.port = port
#         self.username = username
#         self.password = password
#         self.db = db
#
#     def fetch(self):
#         pass
#
#     def modify(self):
#         pass
#
#     def remove(self):
#         pass
#
#     def create(self):
#         self.hostname
#         self.port
#
# obj = Foo('192.168.0.80',22,'tony','123456','new')
# obj.create()

#方式二 面向对象的继承
#创建三个游戏人物

# class Person:
#     def __init__(self,name,gender,age,figure):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.figure = figure
#
#     def grassland(self):
#         '''
#         丛林战斗损耗200战斗力
#         '''
#         self.figure = self.figure - 200
#
#     def practice(self):
#         '''
#         自我修炼模式，增长100战斗力
#         '''
#         self.figure = self.figure + 100
#
#     def incest(self):
#         '''
#         多人游戏，消耗战斗力500
#         '''
#         self.figure = self.figure - 500
#
#     def detail(self):
#         '''
#         当前对象的详细情况
#         '''
#         status = "姓名：%s; 性别: %s; 年龄：%s；战斗力:%s"%(self.name,self.gender,self.age,self.figure)
#         print(status)
#
#
# #点击创建角色
# jack = Person('杰克','男',22,1000)
# tony = Person("托尼","男",18,1200)
# dong = Person("安东尼尼","女",20,2000)
# bo = Person("博多多","女",19,2500)
#
# jack.detail()
# tony.detail()
# dong.detail()
# bo.detail()

#类的继承

# class F:
#     def f1(self):
#         print("i am f1")
#
# class S(F):
#     def f2(self):
#         print("i am f2")
#
# obj = S()
# obj.f2()
# obj.f1()

# class M(object):
#     pass
#
# class S(M):
#     pass

# class A:
#     def f1(self):
#         print ("A.f1")
#
# class B:
#     def f1(self):
#         print ("B.f1")
#
# class C(A):
#     def f2(self):
#         print ("C.f1")
#
# class D(C,B):
#     pass
#
# d = D()
# d.f1()

class D(object):
    def bar(self):
        print('D.bar')

class C(D):
    def bar(self):
        print('C.bar')

class B(D):
    pass

class A(B,C):
    pass

a = A()
a.bar()























