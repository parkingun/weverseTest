from Utilities.DriverSetting import DriverSetting
from Config import Variable
from Pages.LoginPage import Login
from Pages.BasePage import BasePage
from Pages.MainPage import mainPage
from API.GetAccountInfo import getAccount
from Function.ExtractCookieData import get_cookie_value

class Test_Login(DriverSetting, BasePage):

    # 현재 테스트에 필요한 변수 정의
    baseURL = Variable.BASE_URL
    email = Variable.ACCOUNTS["test1"]["email"]
    password = Variable.ACCOUNTS["test1"]["password"]

    def test_login(self):

        self.driver.get(self.baseURL)

        # 테스트에 사용할 페이지 객체 생성
        main_Page =  mainPage(self.driver)
        login_Page = Login(self.driver)

        # 메인 페이지에서 로그인 화면으로 이동 케이스
        main_Page.test_Connect_Signin()

        # 로그인 수행
        login_Page.test_Login(self.email, self.password)

        # 로그인 후 프로필 페이지로 이동
        main_Page.test_Connect_Profile()

        # 현재 브라우저의 쿠키를 가져옴
        cookies = self.driver.get_cookies()

        # 쿠키에서 필요한 토큰 및 디바이스 ID 추출
        accessToken = get_cookie_value(cookies, "we2_access_token")
        deviceId = get_cookie_value(cookies, "we2_device_id")

        # API를 호출하여 계정 정보의 응답을 response에 저장
        response = getAccount(accessToken, deviceId)

        print("*******************************************************************")
        print(f" ID = {self.email}, PW = {self.password}, WID = {response["wid"]} ")
        print("*******************************************************************")
