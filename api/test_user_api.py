import json
import pytest
import requests
from api_auto.common import base_data
from api_auto.common import MyEncoder


# def test_fix(self):
#     print('测试登陆夹具')
def test_createSettlementorder(get_cookies, get_headers):
    # print(get_cookies)
    print(get_headers)
    resp = requests.post(base_data.base_url + '/purchaser/trade/invoiceOrder/asyncStandardCreate',
                         json=base_data.createSettlementorder, cookies=get_cookies)
    # print(resp.cookies)
    print(resp.text)
    print(resp.status_code)


def test_createOrder(get_cookies, get_headers):
    # print(get_cookies)
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(base_data.createOrder, ensure_ascii=False, sort_keys=True, indent=4)
    # print(get_headers)
    resp = requests.post(base_data.base_url + '/purchaser/trade/order/createSubmit', json=data, cookies=get_cookies)
    # print(resp.cookies)
    print(resp.text)
    print(resp.status_code)


if __name__ == "__main__":
    pytest.main()
