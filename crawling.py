from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver_path = ChromeDriverManager().install()

# 웹 드라이버 초기화
driver = webdriver.Chrome(options=chrome_options)

# 웹 사이트 열기
driver.get("https://www.interpark.com/")

# 현재 창의 핸들 기억하기
main_window_handle = driver.current_window_handle

# 클래스가 "header_myMenu__KNxdL"인 요소의 하위에 있는 모든 <li> 요소를 선택
list_items = driver.find_elements(By.CSS_SELECTOR, '[class^="header_myMenu"]')


# 첫 번째 <li> 요소에 대한 작업 수행
if list_items:
    first_li = list_items[0]
    # <li> 요소 안에 있는 <a> 요소를 찾기
    link_element = first_li.find_element(By.TAG_NAME, 'a')
    
    # <a> 요소를 클릭하여 새 창 열기
    link_element.click()

    # 모든 창 핸들 가져오기
    all_window_handles = driver.window_handles

    # 새로 열린 창으로 전환
    for window_handle in all_window_handles:
        if window_handle != main_window_handle:
            driver.switch_to.window(window_handle)

    # 여기에서 새로 열린 창에 대한 작업 수행
    # 예: 로그인 정보 입력
    username_field = driver.find_element(By.ID, "userId")
    password_field = driver.find_element(By.ID, "userPwd")

    username_field.send_keys("bigsmileday")
    password_field.send_keys("genius88@@")

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.ID, "btn_login")
    login_button.click()

    # 새로운 탭으로 이동
    driver.execute_script("window.open('', '_blank');")
    new_tab_handle = driver.window_handles[-1]
    driver.switch_to.window(new_tab_handle)

    # 새로 열린 탭에 주소로 이동
    driver.get("https://tickets.interpark.com/")

    # 새로 열린 탭에서 필요한 작업 수행
