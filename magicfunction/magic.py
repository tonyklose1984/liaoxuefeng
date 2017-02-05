#coding:utf-8

# class Student(object):
#     def __init__(self,name):
#         self.name  = name
#     def __str__(self):
#         return "My Name is:%s"%self.name
#

# s = Student('Jack')
#
# print s

#__iter__

# class Fib(object):
#     def __init__(self):
#         self.a,self.b = 0,1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         self.a,self.b = self.b,self.a+self.b
#         if self.a > 10000:
#             raise StopIteration()
#         return self.a
#
# for n in Fib():
#     print n

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n,int):
#             a,b = 1,1
#             for x in range(n):
#                 a,b = b,a+b
#             return a
#         if isinstance(n,slice):
#             start = n.start
#             stop = n.stop
#             a,b = 1,1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a,b = b,a+b
#             return L
#
# f = Fib()
#
# print f[0:10]

#__getattr__属性

# class Student(object):
#     def __init__(self):
#         self.name = "Michael"
#
#     def __getattr__(self, attr):
#         if attr == "score":
#             return 99
#         elif attr == "age":
#             return lambda:25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
#
# s = Student()
# print s.name
# print s.score
# print s.age()
# print s.abc

# class Chain(object):
#     def __init__(self,path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain("%s/%s"%(self._path,path))
#
#     def __str__(self):
#         return self._path
#
# print Chain().status.user.timeline.list
# print Chain().users('michael').repos

#__call__

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self):
#         print("My name is %s"%self.name)
#
# s = Student('Michael')
#
# s()
#
# print callable(Student('Michael'))
# print callable(max)
# print callable([1,2,3])
# print callable(None)
# print callable("string")

# class Chain(object):
#     def __init__(self,url=''):
#         self._url = url
#
#     def user(self,username):
#         return Chain('GET /user/:%s'%username)
#
#     def __getattr__(self, attr):
#         return Chain('%s/%s'%(self._url,attr))
#
#     def __str__(self):
#         return self._url
#
# print Chain().user('Micheal').repo

# class Chain(object):
#     def __getattr__(self, attr):
#         if attr == "users":
#             return lambda user:Chain("%s/users/:%s"%(self.__path,user))
#         else:
#             return Chain("%s/%s"%(self.__path,attr))
#
# print Chain()

#type()使用元类

# from hello import Hello
#
# h = Hello()
# h.hello()
# print(type(Hello))
# print(type(h))

# def fn(self,name='world'):
#     print('Hello, %s.'%name)
#
# Hello = type('Hello',(object,),dict(hello=fn))
#
# h = Hello()
# h.hello()
#
# print(type(Hello))
# print(type(h))

# def sayit(self,word):
#     print("say something: %s"%word)
#
# Say = type('Say',(object,),dict(saying=sayit))
#
# b = Say()
# b.saying("what is this")

#metaclass 元类
# class ListMetaclass(type):
#     def __new__(cls, name,bases,attrs):
#         attrs['add'] = lambda self,value:self.append(value)
#         return type.__new__(cls,name,bases,attrs)
#
# class MyList(list):
#     __metaclass__ = ListMetaclass
#
# L= MyList()
# L.add(1)
# print L

# class ObjectCreator(object):
#     pass
#
# my_object = ObjectCreator()
#
# print my_object














