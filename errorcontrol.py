# def div(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("Error :b should not be 0!!")
#     except Exception as e:
#         print("Unexpected Error:{}".format(e))
#     else:
#         print("Run into else only when everything goes well")
#     finally:
#         print("Always run into finally block")
#
# div(2,0)
# print("_____________")
# div(2,'bad type')
# print("_____________")
# div(1,2)


# def div(a,b):
#     try:
#         print(a/b)
#     except(ZeroDivisionError,TypeError) as e:
#         print(e)
#
# div("a"/"b")

def f1():
    print(1/0)

def f2():
    try:
        f1()
    except Exception as e:
        print("能除吗你个傻吊")

f2()























