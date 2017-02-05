import pickle
import json
import datetime

def sayHi():
    yield 'hehe1'
    yield 'hehe2'
    yield 'hehe3'

class Test(object):
    def __init__(self,name):
        self.name = name

t = Test("alex")
t2 = Test("tony")

# print(t.__next__()),
print(type(t))
print(pickle.dumps(t))
print(json.dumps(t))
print(pickle.dumps(datetime.datetime.now()))