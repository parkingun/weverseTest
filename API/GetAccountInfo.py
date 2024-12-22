import requests

""" 계정 정보를 얻기 위한 API """
def getAccount(accessToken, deviceId):

    url = "https://global.apis.naver.com/weverse/wevweb/users/v1.0/users/me?appId=be4d79eb8fc7bd008ee82c8ec4ff6fd4&language=ko&os=WEB&platform=WEB&wpf=pc&wmsgpad=1734791280426&wmd=2VZoAA%2FY2NXN3LV2sumuAxWH2q4%3D"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {accessToken}",
        "Referer": "https://weverse.io/",
        "wev-device-id": f"{deviceId}",
        "wev-open-community": "A"
    }

    response = requests.get(url, headers=headers, verify=False)

    # 요청 출력
    # print("Request URL:", response.request.url)
    # print("Request Headers:", response.request.headers)
    # print("Response Status Code:", response.status_code)
    # print("Response Text:", response.text)

    return response.json()
