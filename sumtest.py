#coding:utf-8
#通常情况的求和函数
# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax += n
#     return ax
#
# print(calc_sum(1,2,3,4))

#如果不需要立即求和返回求和函数
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax += n
#         return ax
#     return sum
#
# f1 = lazy_sum(1,3,5,7,9)
# f2 = lazy_sum(1,3,5,7,9)
#
# print(f1 == f2)

#闭包
# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
# f1,f2,f3 = count()
#
# print(f1())
# print(f2())
# print(f3())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
#
# f1,f2,f3 = count()
#
# print(f1())
# print(f2())
# print(f3())

#匿名函数
# print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
#
# f = lambda x:x*x
# print(f)
# print(f(5))
#
# def build(x,y):
#     return lambda: x*x+y*y
#
# print(build(4,5)())

# def count():
#     fs = []
#     for i in range(1,4):
#         fs.append(lambda : i*i)
#     return fs
#
# f1,f2,f3 = count()
#
# print(count())
# print(f1())
# print(f2())
# print(f3())

# def count():
#     fs = []
#     for i in range(1,4):
#         def g(j):
#             return lambda :j*j
#         fs.append(g(i))
#     return fs
# f1,f2,f3 = count()
# print(f1())
# print(f2())
# print(f3())

# def foo():
#     return 'beginman'
# print(foo())
#
# print((lambda :'beginman')())

# bar = lambda :'beginman'
#
# print(bar())
#
# add = lambda x,y,z:x*2+y*3+z*4
#
# print(add(1,2,3))

# sum2 = lambda x,y=10:x+y
#
# print(sum2(1,100))










































