import requests
import json
import time
import base64
from urllib.parse import quote
import hashlib

send_url = "http://120.77.221.146/sms-inbox/api/send"

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

content = '【海纳亚洲】您好，您的报名已确认！感谢您报名参加SIG与薪智联合举办的线上活动，活动将如期于2021年11月3日14:00以直播的形式呈现，您可点击此链接https://mudu.tv/live/watch/technology?id=m3yn25ro进入直播间，期待您的支持与参与。'
content = quote(content, 'utf-8')

mobiles = '18721702068'

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
