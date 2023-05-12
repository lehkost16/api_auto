# 基础数据
from sqlalchemy import false, null, true
import pymysql
import pandas as pd

#
try:
    config = {
        'host': '0.0.0.0',
        'port': 3306,
        'user': 'root',
        'passwd': '1201',
        'db': 'account',
        'charset': 'utf8mb4',
        "cursorclass": pymysql.cursors.DictCursor
    }
    conn = pymysql.connect(**config)
    cur = conn.cursor()
except:
        print('connect error')
        exit()
def getloginInfo():

    sql = 'select * from user_info where id =1'
    # insert into user_info (user_name,passwd) values("jxg100001","IpKBhJnvLFai+%c2"
    cur.execute(sql)
    result = cur.fetchone()
    return result

pur_account = getloginInfo()['user_name']
pur_passwd = getloginInfo()['passwd']
pur_url = getloginInfo()['url']
http_t = getloginInfo()['http']


cur.close()  # 关闭游标
conn.close()  # 关闭数据库连接

# getloginInfo()
# def pwdDncryption(string):
#



