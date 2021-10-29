import pymysql


def clear_data(cycle):
    db = pymysql.connect(host='localhost', user='root', password='Sus9uehanna!', db='portfolio')
    cursor = db.cursor()
    if cycle == 1:
        cursor.execute("update auto_message_portfoliocompany set status=FALSE where cycle= 'monthly'")
    else:
        cursor.execute("update auto_message_portfoliocompany set status=FALSE")
    db.commit()
    db.close()

clear_data(1)

