# base_data

import pymysql

try:
    config = {
        'host': '172.20.0.3',
        'port': 3306,
        'user': 'root',
        'passwd': '1201',
        'db': 'acc_info',
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

print(getloginInfo())

conn.commit() # 提交操作到数据库
cur.close()  # 关闭游标
conn.close()  # 关闭数据库连接



## zhangfeipaoma