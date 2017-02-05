import hashlib

#英文字符串
m = hashlib.md5(b'wupeiqi')
m.update(b'admin')
md5value = m.hexdigest()
print(md5value)

#中文字符串
data = '我是'
m = hashlib.md5(data.encode(encoding='gb2312'))
print(m.hexdigest())

#高级加密模块
import hmac
trans_5C = bytes((x ^ 0x5C) for x in range(256))
print(trans_5C)
#3版本必须加b
h = hmac.new(b'wupeiqi')
h.update(b'hellowo')
print(h.hexdigest())


