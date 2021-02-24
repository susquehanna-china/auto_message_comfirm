from django.test import TestCase

# Create your tests here.
import base64
import hashlib
import time
from urllib.parse import quote
account = 'http135993'
now = time.localtime()
timelist = [now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec]
timenow = ''
for i in timelist:
    if len(str(i)) == 1:
        timenow = timenow + '0' + str(i)
    else:
        timenow += str(i)

nonce = base64.b64encode(bytes(account + ',' + timenow, 'utf-8'))
print(nonce)

content = '这是一条测试短信'
print(quote(content, 'utf-8'))

mobiles = '18721702068'

key = '4fae0b045'

string1 = sorted([key, timenow, account])
out = ''
for i in string1:
    out += i
signature = hashlib.sha1(out.encode('utf-8')).hexdigest()
print(signature)