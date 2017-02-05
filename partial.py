#偏函数
import functools
#  def int2(x,base=2):
#     return int(x,base)
#
# print(int2('10101010'))

# import functools
# int2 = functools.partial(int,base=2)
#
# print(int2('1000000'))
#
# int2 = lambda x,base=2:int(x,base)
#
# print(int2('1000000'))


# max2 = functools.partial(max,10)
#
# l = max2(5,6,7)
# print(l)

# def add(a,b):
#     return a+b
#
# print(add(4,2))
#
# plus3 = functools.partial(add,3)
# plus5 = functools.partial(add,5)
#
# print(plus3(4))
#
# print(plus3(7))
#
# print(plus5(10))

# def get(self,request,*args,**kwargs):
#     context = {
#         'ua_filter':functools.partial(get_useragent,**{"request":request})
#     }
#     self.render('index.html',context)
#
# def say(name,age):
#     print(name,age)
#
# func = functools.partial(say,age=5)
#
# func('the5fire')

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         self.nums = nums
#         self.target = nums[0] + nums[1]
#         return nums[:2]
#
#
# a = Solution()
#
# print(a.twoSum([1, 2, 3, 4], 3))

from module1 import main
main()



















































