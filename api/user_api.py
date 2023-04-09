import pytest

@pytest.mark.usefixtures("get_token")
class Test_login():
    def test_fix(self):
        print('测试登陆夹具')


if __name__ == "__main__":
    pytest.main()
