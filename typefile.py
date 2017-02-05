# import types
#
# def fn():
#     pass
#
# print(type(fn) == types.FunctionType)
#
# print(type(abs) == types.BuiltinFunctionType)
#
# print(type(lambda x:x) == types.LambdaType)
#
# print(type((x for x in range(10))) == types.GeneratorType)
#
# print(isinstance(b'a',bytes))
#
# print(isinstance([1,2,3],(tuple)))
#
# print(len('ABC'))
#
# print('ABC'.__len__())
#
# class MyDog(object):
#     def __len__(self):
#         return 100
#
# dog = MyDog()
#
# print(len(dog))

# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#     def power(self):
#         return self.x*self.x
#
# obj = MyObject()
#
# print(obj.power())
#
# print(hasattr(obj,'x'))
#
# print(obj.x)
#
# print(hasattr(obj,'y'))
#
# setattr(obj,'y',19)
#
# print(hasattr(obj,'y'))
#
# print(getattr(obj,'y'))
#
# print(getattr(obj,'z',404))
#
# print(hasattr(obj,'power'))
#
# print(getattr(obj,'power'))
#
# fn = getattr(obj,'power')
#
# print(fn())
#
# def readImage(fp):
#     if hasattr(fp,'read'):
#         return readImage(fp)
#     return None

# class Field(object):
#     def __init__(self,name,column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return '<%s:%s>'%(self.__class__.__name__,self.name)
#
# class StringField(Field):
#     def __int__(self,name):
#         super(StringField,self).











































