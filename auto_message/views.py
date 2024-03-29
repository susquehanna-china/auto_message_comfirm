from django.shortcuts import render, HttpResponse
from .models import PortfolioCompany
from django.template import loader
from django.views.decorators import csrf
from django.db.models import F
from django.http import HttpResponse
from rest_framework.response import Response
import requests
import json
import time
import base64
from urllib.parse import quote
import hashlib
from rest_framework.views import APIView
import datetime

# Create your views here.

def return_message(content, target):
    send_url = "http://120.77.221.146/sms-inbox/api/send"

    account = 'http135993'
    now = time.localtime()
    time_list = [now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec]
    if time_list[3] + 8 > 24:
        time_list[3] = time_list[3] - 16
    else:
        time_list[3] = time_list[3] + 8
    time_now = ''
    for i in time_list:
        if len(str(i)) == 1:
            time_now = time_now + '0' + str(i)
        else:
            time_now += str(i)
    nonce = base64.b64encode(bytes(account + ',' + time_now, 'utf-8')).decode()

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


def report(request):
    print(request)
    if request.method == 'POST':
        result = json.loads(request.body)
        for item in result:
            print(item)
            if item['content'] == '1':
                tele_number = item['mobile']
                try:
                    company = PortfolioCompany.objects.get(phone=tele_number)
                    if not company.status:
                        company.status = True
                        if company.commit_record:
                            company.commit_record += str(
                                str(time.localtime().tm_year) + '/' + str(time.localtime().tm_mon) + ';')
                        else:
                            company.commit_record = str(
                                str(time.localtime().tm_year) + '/' + str(time.localtime().tm_mon) + ';')
                        company.save()
                    return_message('【海纳亚洲】确认成功，感谢您的配合！', tele_number)
                except PortfolioCompany.DoesNotExist:
                    print('error')

            else:
                return_message('【海纳亚洲】您发送的确认信息有误，如已经发送相关文件请回复1', item['mobile'])

        return HttpResponse('ok')
    else:
        result = request
        print(result)
    return HttpResponse('method error')


def DIY_message(number, text):
    send_url = "http://120.77.221.146/sms-inbox/api/send"

    account = 'http135993'

    content = '【海纳亚洲】' + text
    content = quote(content, 'utf-8')

    mobiles = number
    key = '4fae0b045'

    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    time_list = [now.year, now.month, now.day, now.hour, now.minute, now.second]
    time_now = ''
    for i in time_list:
        if len(str(i)) == 1:
            time_now = time_now + '0' + str(i)
        else:
            time_now += str(i)
    print(time_now)
    #x = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    #print(x.year, x.month, x.day, x.hour, x.minute, x.second)
    nonce = base64.b64encode(bytes(account + ',' + time_now, 'utf-8')).decode()

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




class DIYMessageSend(APIView):
    def post(self, request):
        if request.data:
            print(request.data['number'])
            print(request.data['text'])
            print(request.data['code'])

            if request.data['code'] == 'Sus9uehanna!':
                DIY_message(request.data['number'], request.data['text'])
            else:
                return Response(0)
            return Response(0)
        else:
            return Response(0)
