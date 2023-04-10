import pytest
import requests

# from ..common import base_data
from api_auto.common import base_data

    # def test_fix(self):
    #     print('测试登陆夹具')
def test_creat(get_cookies,get_headers):
    print(get_cookies)
    resp = requests.post(base_data.base_url +'/purchaser/trade/order/createSubmit', data=base_data.creatOrder,headers=get_headers,cookies=get_cookies)
    # print(resp.cookies)
    print(resp.url)
    print(resp.status_code)
    assert resp.text
if __name__ == "__main__":
    pytest.main()
