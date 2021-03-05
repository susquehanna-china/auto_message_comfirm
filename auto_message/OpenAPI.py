import requests
import json
import time
import base64
from urllib.parse import quote
import hashlib

send_url = "http://47.112.247.219/sms-inbox/api/send"

account = 'http135993'
now = time.localtime()
time_list = [now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec]
time_now = ''
for i in time_list:
    if len(str(i)) == 1:
        time_now = time_now + '0' + str(i)
    else:
        time_now += str(i)
nonce = base64.b64encode(bytes(account + ',' + time_now, 'utf-8')).decode()

content = '【海纳亚洲】SIG投后提醒您确认是否发送本月/本季财报，如已发送请回复1'
content = quote(content, 'utf-8')

mobiles = '13858090451'

key = '4fae0b045'
string1 = sorted([key, time_now, account])
out = ''
for i in string1:
    out += i
signature = hashlib.sha1(out.encode('utf-8')).hexdigest()

data = {
    "nonce": nonce,
    "mobiles": mobiles,
    "sendContent": content,
    "signature": signature
}
headers = {'Content-Type': "application/json"}
test = requests.post(url=send_url, headers=headers, data=json.dumps(data))
print(test.text)
