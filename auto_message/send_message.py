import sqlite3
import time


def get_data():
    conn = sqlite3.connect('../db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('select * from auto_message_portfoliocompany')
    data = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return data


judge = 0
while True:
    if time.localtime().tm_sec == 10 and judge == 0:
        judge = 1
        data = get_data()
        print(data)
        time.sleep(2)
        judge = 0

