import json
f = open("data_to_qq.txt",'rb')

name = json.loads(f.read().decode("utf-8"))
f.close()
print(name['alex'])
print(type(name))
