프로젝트: 위버스 회원가입 후 로그인하여 WID 추출하는 케이스를 구현하라!

**프로젝트 버전 정보**
- **Python**: 3.12.8
- **Selenium**: 4.27.1

**1. 폴더구조**
- API (API를 모아놓는 폴더)
  - GetAccountInfo (계정 정보를 가져오기 위한 API)
- Config (URL, 변수 등의 설정 관련된 파일의 폴더)
  -  variable (변수 정의 - 계정의 경우에는 딕셔너리로 정의하여 추가해서 사용가능)
- Function (재사용 가능한 함수 파일의 폴더)
  - getCookie
- Pages (페이지별로 필요한 elements를 생성하고 이벤트와 테스트를 만들어 놓은 폴더)
  - BasePage (모든 페이지에서 공통적으로 사용하는 이벤트를 모은 폴더)
  - LoginPage
  - MainPage
- Reports (테스트 결과 만들어지는 리포트를 모은 폴더)
- TestCase (테스트 케이스를 모은 폴더)
  - Test_Login 
- Utilities (다양한 역할을 할 수 있는 파일을 모은 폴더)
  - DriverSetting (webdriver에 대한 설정)
- Runner.py (테스트를 실행하여 리포트까지 생성되는 파일.)

**2. 코드 컨벤션**
- 폴더와 파일명의 처음은 대문자로 시작한다.
- 로컬 변수는 카멜케이스로 사용한다. (예: testData)
- Variable에 정의하는 상수는 모두 대문자로 정의한다.
