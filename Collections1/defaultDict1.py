from collections import defaultdict
#默认字典方法
# dic = {'k1':[]}
#
# if 'k1' in dic.keys():
#     dic['k1'].append(1)
# else:
#     dic['k1'] = [1,]
#
# my_dict = defaultdict(list)
# my_dict['k1'].append(1)
# print(my_dict['k1'])

dic = defaultdict(list)
dic['k1'].append(1)
print(dic)