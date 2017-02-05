#coding:utf-8

# try:
#     print("try...")
#     r = 10/2
#     print('result',r)
# except ZeroDivisionError as e:
#     print('except',e)
# finally:
#     print('finally')
# print('END')

#多except捕获错误

# try:
#     print('try...')
#     r = 10 / 2
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('除数不能为零！',e)
# else:
#     print('no error')
# finally:
#     print('finally')
# print('END')

# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error',e)
#     finally:
#         print('finally...')
#
# main()

# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main():
#     bar("0")
#
# main()

#loggin日志模块
# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s)*2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

#抛出错误

# class FooError(ValueError):
#     print("除数错误!")
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value" %s'%s)
#     return 10 / n
#
# foo('0')

#raise抛出
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalid value: %s'%s)
#     return 10 / n
#
# def bar():
#     try:
#         foo("0")
#     except ValueError as e:
#         print("ValueError!")
#         raise
#
# bar()

# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')

#assert 断言

# def foo(s):
#     n = int(s)
#     assert n != 0,'n is zero!'
#     return 10 / n
#
# def main():
#     foo("0")
#
# main()

#logging日志记录
#这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件
# import logging
# logging.basicConfig(level=logging.INFO)
#
# s = '0'
# n = int(s)
# logging.info("n = %d"%n)
# print(10/n)
























































