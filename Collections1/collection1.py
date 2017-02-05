from collections import Counter
#
# dic = {'k1':123,"k2":123,"k3":12}
#
# c1 = Counter(dic)
#
# print(c1)
#
# c = Counter('abcdabcdabcdabaf')
#
# print(c.most_common(5))
#
# d = Counter('simsalabim')
# c.update(d)
# print(c)

c1 = Counter('aabc')
c2 = Counter('aab')
c1.update(c2)
print(c1)





