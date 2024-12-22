import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from datetime import date

class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # 이메일 input xpath
    email_Input = '//*[@name="userEmail"]'

    # 비밀번호 input xpath
    password_Input = '//*[@name="password"]'

    # [로그인] / [이메일로 계속하기] 버튼 xpath
    login_Button = '//*[@type="submit"]'

    # 미인증 계정 모달 확인 xpath
    notAuthEmail = '//body/div//*[contains (text(), "미인증 계정입니다.")]'

    # [이메일 재전송] 버튼 xpath
    resendEmail = '//footer//*[contains(text(), "이메일 재전송")]'

    # 로그인 후 메인페이지 이동 확인을 위한 xpath
    logoBtn = '//*[contains(@class, "HeaderView_logo")]'

    """ 로그인 테스트 """
    def test_Login(self, email, passowrd):
        # 이메일 입력
        self.send_keys(By.XPATH, self.email_Input, email)

        # [이메일로 계속하기] 버튼 클릭
        self.click(By.XPATH, self.login_Button)

        # 비밀번호 입력
        self.send_keys(By.XPATH, self.password_Input, passowrd)

        # [로그인] 버튼 클릭
        self.click(By.XPATH, self.login_Button)

        # 로그인 성공 후 메인페이지 로고 확인
        self.find_element(By.XPATH, self.logoBtn)


    """ 회원가입 테스트 """
    def test_Signup(self, email, password):
        # 이메일 입력
        self.send_keys(By.XPATH, self.email_Input, email)

        # [이메일로 계속하기] 버튼 클릭
        self.click(By.XPATH, self.login_Button)

        # 미인증 계정 시 처리
        if self.find_element(By.XPATH, self.notAuthEmail):
            self.click(By.XPATH, self.resendEmail)

        # 인증과정~
        time.sleep(1)
