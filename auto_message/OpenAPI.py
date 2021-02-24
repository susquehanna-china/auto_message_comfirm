import requests

send_url = "http://47.112.247.219/sms-inbox/api/send"

test_url = 'http://127.0.0.1:8000/portfolio_comfirm/api'

test = requests.get('http://127.0.0.1:8000/portfolio_comfirm/api?data=123')
print(
    test.text
)
