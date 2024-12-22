import unittest
from selenium import webdriver

class DriverSetting(unittest.TestCase):

    def setUp(self):
        print("테스트 시작")

        # 브라우저 옵션 설정
        options = webdriver.ChromeOptions()
        # 브라우저 최대화 옵션 추가
        options.add_argument("--start-maximized")
        # 브라우저 실행
        self.driver = webdriver.Chrome(options=options)

        print("브라우저 설정 완료")

    def tearDown(self):
        # 브라우저 닫기
        self.driver.quit()
        print("테스트 완료")
