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


