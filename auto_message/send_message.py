import pymysql
import time

def get_data(cycle):
    db = pymysql.connect(host='localhost', user='root', password='Sus9uehanna!', db='portfolio')
    cursor = db.cursor()
    if cycle == 1:
        cursor.execute(
            "select tele_number from auto_message_portfoliocompany where cycle = 'monthly' and status = false ")
        result = cursor.fetchall()
        return [i[0] for i in result]
    else:
        cursor.execute(
            "select tele_number from auto_message_portfoliocompany where cycle = 'quarter' and status = false ")
        result = cursor.fetchall()
        return [i[0] for i in result]


while True:
    if time.localtime().tm_min % 2 == 0:
        print(get_data(1))
        time.sleep(60)
    else:
        print(get_data(0))
        time.sleep(60)
