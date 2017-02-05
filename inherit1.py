#__str__
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#         print("Student object (name: %s)" % self.name)
#
# Student("Mike")
#
# s = Student("Micheal")
#
# s

#__iter__ 循环迭代
# class Fib(object):
#     def __init__(self):
#         self.a,self.b = 0,1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a,self.b = self.b,self.a+self.b
#         if self.a > 100000:
#             raise StopIteration()
#         return self.a
#
#
# for n in Fib():
#     print(n)

#__getitem__
# class Fib(object):
#     def __getitem__(self,n):
#         a,b = 1,1
#         for x in range(n):
#             a,b = b,a+b
#         return a
#
# f = Fib()
# print(f[0:5])

#利用判断设置切片或者int类型:
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a

        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b = b,a+b
            return L

f = Fib()

print(f[0:5])

print(f[:10:2])













