import pytest
import requests

from common import base_data


# 夹具client

# pur_passwd_bytes = base_data.pur_passwd.encode('utf-8')
#
# pur_passwd = base_data.pur_passwd
@pytest.fixture(scope='class')
def get_cookies():
    user_data = {
        "username": base_data.pur_account,
        "password": base_data.pur_passwd,
        "imageCode": "0000"
    }
    session = requests.session()
    resp = session.post(base_data.base_url + "/userauth/cloLogin/purchaser_login", json=user_data, allow_redirects=False)  ##获取登陆接口
    # session.post(base_data.base_url + "/userauth/cloLogin/purchaser_login", json=user_data)
    cookies = dict(resp.cookies)
    # headers =resp.headers
    yield cookies
    # cookies = resp.cookies.get_dict()
    # cookies = dict(resp.cookies)
    # print('cookie', cookies)
    # response_index = requests.get(base_data.base_url, cookies=cookies)
    # print('Response Status', response_index.status_code)
    # print('Response URL', response_index.url)

    # print(resp.cookies)
    # cookiejar = resp.cookies.get_dict()
    # print('first cookie', cookiejar)
    # x = resp.json()
    # print('there is a token in resp', resp.json())
    # print('the data of token', x['user_data']['token'])
    # cookiejar['Authorization'] = x['user_data']['token']
    # print('the cookie has add a token', cookiejar)
    # cookie_string = ';'.join(str(x) + '=' + str(y) for x, y in cookiejar.items())
    # headers = {
    #     'Cookie': cookie_string
    # }
    # print(cookie_string)
    # print(headers)
@pytest.fixture(scope='class')
def get_headers():
    user_data = {
        "username": base_data.pur_account,
        "password": base_data.pur_passwd,
        "imageCode": "0000"
    }
    session = requests.session()
    resp = session.post(base_data.base_url + "/userauth/cloLogin/purchaser_login", json=user_data,
                        allow_redirects=False)
    headers = resp.headers
    yield headers

# get_token()
# @pytest.mark.usefixtures('get_token')

