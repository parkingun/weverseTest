""" 쿠키값에서 원하는 데이터 추출하기 위한 함수 """
def get_cookie_value(cookies, target_name):
    # filter를 사용해 원하는 쿠키 항목을 찾고, 첫 번째 항목의 value 값을 반환
    filtered_items = list(filter(lambda item: item['name'] == target_name, cookies))
    return filtered_items[0]['value'] if filtered_items else None
