import requests

from common import base_data


# 夹具client

# pur_passwd_bytes = base_data.pur_passwd.encode('utf-8')
#
# pur_passwd = base_data.pur_passwd

def get_token():
    user_data = {
        "username": base_data.pur_account,
        "password": base_data.pur_passwd,
        "imageCode": "0000"
    }

    resp = requests.post(base_data.base_url + "/userauth/cloLogin/purchaser_login", json=user_data)
    # print(resp.cookies)
    cookiejar = resp.cookies.get_dict()
    print('first cookie', cookiejar)
    x = resp.json()
    print('there is a token in resp', resp.json())
    print('the data of token', x['user_data']['token'])
    cookiejar['Authorization'] = x['user_data']['token']
    print('the cookie has add a token', cookiejar)
    cookie_string = ';'.join(str(x) + '=' + str(y) for x, y in cookiejar.items())
    headers = {
        'Cookie': cookie_string
    }
    print(cookie_string)


get_token()
