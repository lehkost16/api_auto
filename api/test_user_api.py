import os

import allure
import pytest
import requests
import common.base_data as bd


# def test_fix(self):
#     print('测试登陆夹具')
@allure.feature('创建结算单')
def test_createSettlementorder(get_cookies, get_headers): #  test create_settlementorder  work
    print(get_cookies)
    print(get_headers)
    resp = requests.post(bd.pur_url + '/purchaser/trade/invoiceOrder/asyncStandardCreate',
                         json={},cookies=get_cookies)
    print(get_cookies)
    # print(resp.text)
    # print(resp.status_code)

@allure.feature('创建对账单')
def test_createStatement(get_cookies):
    resp =requests.post(bd.pur_url+'/purchaser/trade/settlementOrder/ar/batchCreate',json={},cookies=get_cookies)
    print(resp.text)
    print(get_cookies)
    # assert re.search('"code":"success"',resp.text)
    # print('hello')


if __name__ == "__main__":
    pytest.main(['--alluredir','./temp'])
    os.system('allure generate ./temp -o ./report --clean')
