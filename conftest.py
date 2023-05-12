import pytest
import requests

import common.base_data as bd

# login info
user_data = {
    "username": bd.pur_account,
    "password": bd.pur_passwd,
    "imageCode": "0000"
}
# 夹具client

# pur_passwd_bytes = base_data.pur_passwd.encode('utf-8')
#
# pur_passwd = base_data.pur_passwd
@pytest.fixture(scope='class')
def get_cookies():

    session = requests.session()
    resp = session.post(bd.http_t+'://'+bd.pur_url + "/userauth/cloLogin/purchaser_login", json=user_data,
                        allow_redirects=False)  ##获取登陆接口
    # session.post(base_data.base_url + "/userauth/cloLogin/purchaser_login", json=user_data)
    cookies = dict(resp.cookies)
    # headers =resp.headers
    yield cookies
    # cookies = resp.cookies.get_dict()
    # cookies = dict(resp.cookies)
    print('cookie', cookies)
    # response_index = requests.get(base_data.base_url, cookies=cookies)
    # print('Response Status', response_index.status_code)
    # print('Response URL', response_index.url)


@pytest.fixture(scope='class')
def get_headers():

    session = requests.session()
    resp = session.post(bd.http_t+'://'+bd.pur_url + "/userauth/cloLogin/purchaser_login", json=user_data,
                        allow_redirects=False)
    headers = resp.headers
    yield headers

# get_token()
# @pytest.mark.usefixtures('get_token')
