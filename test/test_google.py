from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.get("http://google.com")
    driver.quit()
