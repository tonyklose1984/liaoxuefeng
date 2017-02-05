#普通字典实现排列
# values = [11,22,33,44,55,66,77,88,99,90]
# my_dict = {'k1':[33],'k2':[22]}
# for value in values:
#     if value > 66:
#         if 'k1' in my_dict:
#             my_dict['k1'].append(value)
#         else:
#             my_dict['k1'] = [value]
#     else:
#         if 'k2' in my_dict:
#             my_dict['k2'].append(value)
#         else:
#             my_dict['k2'] = [value]
# print(my_dict)

#default字典排序
from collections import defaultdict
values = [11,22,33,44,55,66,77,88,99,90]
my_dict = defaultdict(list)

for value in values:
    if value > 66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)

print(my_dict)
