#coding:utf-8
# class Student(object):
#     name = 'Jack'
#     def __init__(self,name):
#         self.name = name
#
# s = Student('Bob')
#
# s.score = 90
#
# print(s.name)
#
# print(Student.name)
#
# s.name = "Micheal"
#
# print(s.name)
# print(Student.name)
# del s.name
# print(s.name)

# class Student(object):
#     pass
#
# s = Student()
#
# s.name = "Micheal"
#给s添加方法
# def set_age(self,age):
#     self.age =age
#
# from types import MethodType
# s.set_age = MethodType(set_age,s)
# s.set_age(25)
# print(s.age)
#
# s2 = Student()

#给Student绑定方法
# def set_score(self,score):
#     self.score =score
#
# Student.set_score = set_score
#
# s.set_score(100)
# print(s.score)
#
# s2.set_score(99)
# print(s2.score)

#使用__slots__
#限制实例的属性只能有name 和 age
# class Student(object):
#     __slots__=('name','age')
#
# s = Student()
# s.name = 'Micheal'
# s.age = 25
# # s.score = 99
# class GraduStudent(Student):
#     pass
#
# g = GraduStudent()
#
# g.score = 999
# print(g.score)

#使用@property

# class Student(object):
#     def get_score(self):
#         return self._score
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be interger')
#         if value < 0 or value >100:
#             raise ValueError('socre must be between 0-100')
#         self._score = value
#
#
# s = Student()
# s.set_score(60)
# s.set_score('A')
# print(s.get_score())
#
# class Student(object):
#     @property
#     def birth(self):
#         return self._birth,self._age
#
#     @birth.setter
#     def birth(self,value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2016-self._birth
#
#     @age.setter
#     def age(self,value):
#         self._age = value
#
# # s = Student()
# #
# # s.birth = 1964
#
# s1 =Student()
#
# # s1.birth = 1987
#
# s1.age = 33
#
# print(s1.age)


class Screen(object):
    @property
    def width(self):
        return self._widht

    @width.setter
    def width(self, value):
        self._widht = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._widht*self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.width,s.height)
print(s.resolution)

















































































