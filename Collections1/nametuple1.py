from collections import namedtuple

#可命名元组
#1.先创建类 2.实例化类
Mytuple = namedtuple('Mytuple',['x','y','z'])
n = Mytuple(1,2,3)
print(n,n.x,n.y,n.z)
