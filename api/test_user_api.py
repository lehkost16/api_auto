import pytest
import requests
from api_auto.common import base_data

# def test_fix(self):
#     print('测试登陆夹具')
def test_create(get_cookies):
    print(get_cookies)
    resp = requests.post(base_data.base_url +'/purchaser/trade/order/createSubmit', data=base_data.creatOrder,cookies=get_cookies)
    # print(resp.cookies)
    print(resp.url)
    print(resp.status_code)
    assert resp.text
if __name__ == "__main__":
    pytest.main()
