import pymysql
import requests
import json
import time
import base64
from urllib.parse import quote
import hashlib


def clear_data(cycle):
    db = pymysql.connect(host='localhost', user='root', password='Sus9uehanna!', db='portfolio')
    cursor = db.cursor()
    if cycle == 1:
        cursor.execute("update auto_message_portfoliocompany set status=false where cycle= 'monthly'")
    else:
        cursor.execute("update auto_message_portfoliocompany set status=false")
    db.close()


def get_data(cycle):  # cycle = 1 means monthly else means all
    db = pymysql.connect(host='localhost', user='root', password='Sus9uehanna!', db='portfolio')
    cursor = db.cursor()
    if cycle == 1:
        cursor.execute(
            "select phone from auto_message_portfoliocompany where cycle = 'monthly' and status = false and active = "
            "True")
        result = cursor.fetchall()
        db.close()
        out = ''
        for i in result:
            out += str(i[0] + ',')
        return out
    else:
        cursor.execute(
            "select phone from auto_message_portfoliocompany where status = false and active = True")  # all
        result = cursor.fetchall()
        db.close()
        out = ''
        for i in result:
            out += str(i[0] + ',')
        return out


def openapi(target):
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

    content = '【海纳亚洲】SIG投后提醒您请确认是否已将9月/本季度财报及运营数据发送至投后邮箱ChinaPIM@sig.com及相关投资负责人邮箱，' \
              '如有问题可联系咨询Eva Zhang 010-65666830。如已发送请回复1。'
    content = quote(content, 'utf-8')

    mobiles = target

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
    send = requests.post(url=send_url, headers=headers, data=json.dumps(data))
    print(send.text)


while True:
    if time.localtime().tm_mon in [1, 4, 7, 10]:
        #print(get_data(0))
        openapi(get_data(0))
        time.sleep(60 * 60 * 24 * 3)
    else:
        #print(get_data(1))
        openapi(get_data(1))
        time.sleep(60 * 60 * 24 * 3)
