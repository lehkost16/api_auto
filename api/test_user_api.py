import json
import re

import pytest
import requests
# from api_auto.common import base_data
import common.base_data as bd
# from api_auto.common import MyEncoder


# def test_fix(self):
#     print('测试登陆夹具')
def test_createSettlementorder(get_cookies, get_headers): #  test create_settlementorder  work
    # print(get_cookies)
    print(get_headers)
    resp = requests.post(bd.base_url + '/purchaser/trade/invoiceOrder/asyncStandardCreate',
                         json=bd.createSettlementorder, cookies=get_cookies)
    # print(resp.cookies)
    print(resp.text)
    print(resp.status_code)

#
# def test_createOrder(get_cookies, get_headers):#
#     # print(get_cookies)
#     headers = {'Content-Type': 'application/json'}
#     data = json.dumps(bd.createOrder, ensure_ascii=False, sort_keys=True, indent=4)
#     # print(get_headers)
#     resp = requests.post(bd.base_url + '/purchaser/trade/order/createSubmit', json=data, cookies=get_cookies)
#     # print(resp.cookies)
#     print(resp.text)
#     print(resp.status_code)

def test_createStatement(get_cookies):
    resp =requests.post(bd.base_url1+'/purchaser/trade/settlementOrder/ar/batchCreate',json=bd.createStatement,cookies=get_cookies)
    print(resp.text)
    assert re.search('"code":"success"',resp.text)


if __name__ == "__main__":
    pytest.main()
