from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class mainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # 팝업 모달 xpath
    promotionModal = '//*[@id="modal"]'

    # 팝업 모달의 [오늘 하루 보지 않기] 버튼
    promotionCloseBtn = '//*[contains(@class, "BaseModalView_button_container")]//*[text()="오늘 하루 보지 않기"]'

    # 상단 헤더 sign_in 버튼 xpath
    signinBtn = '//*[contains(@class, "HeaderView_link_sign")]'

    # 프로필 버튼 xpath
    profile_Button = '//*[contains (@class, "HeaderView_profile_button")]'

    """ 로그인 버튼 클릭 테스트 """
    def test_Connect_Signin (self):

        # 최초 페이지 진입 시 프로모션 및 모달 출력 시 [오늘 하루 보지 않기] 클릭
        if self.find_element(By.XPATH, self.promotionModal):
            self.click(By.XPATH, self.promotionCloseBtn)

        # [Sign in] 버튼 클릭하여 진입
        self.click(By.XPATH, self.signinBtn)
        time.sleep(1)

    """ 프로필 버튼 클릭하여 진입 """
    def test_Connect_Profile(self):
        # [프로필] 버튼 클릭하여 진입
        self.click(By.XPATH, self.profile_Button)
        time.sleep(1)
