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
    try:
        resp = requests.post(bd.pur_url + '/purchaser/trade/invoiceOrder/asyncStandardCreate',
                             json={},cookies=get_cookies)
        print(get_cookies)
        # print(resp.text)
        # print(resp.status_code)
    except:

        print('create failure')

@allure.feature('创建对账单')
def test_createStatement(get_cookies):
    try:
        resp =requests.post(bd.pur_url+'/purchaser/trade/settlementOrder/ar/batchCreate',json={},cookies=get_cookies)
        # print(resp.text)
        print(get_cookies)
        # assert re.search('"code":"success"',resp.text)
        # print('hello')
    except:
        print('create failure')



@allure.feature('创建付款申请')
def test_create_payorder(get_cookies):
    return 0



if __name__ == "__main__":
    pytest.main(['--alluredir','./temp'])
    os.system('allure generate ./temp -o ./report --clean')
